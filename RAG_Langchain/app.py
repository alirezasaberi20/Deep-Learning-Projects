import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
load_dotenv()

st.title("Chat with Your Document")

# Allow the user to upload a PDF file
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary file so PyPDFLoader can use it
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_path = tmp_file.name

    # --- Document Loading and Indexing ---
    loader = PyPDFLoader(tmp_path)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
        persist_directory="./chroma_db"  # Ensure this directory is writable
    )
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, max_tokens=None, timeout=None)

    # --- Set up Conversation Memory and Chain ---
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conv_chain = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory, verbose=True)

    # Initialize session state for conversation history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display conversation history
    st.markdown("### Conversation History")
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"**User:** {message['content']}")
        else:
            st.markdown(f"**Assistant:** {message['content']}")

    # --- Chat Input and Processing ---
    query = st.chat_input("Say something:")
    if query:
        result = conv_chain({"question": query})
        answer = result["answer"]

        # Update session state with the conversation memory messages
        st.session_state.chat_history = [
            {"role": m.type, "content": m.content} for m in conv_chain.memory.chat_memory.messages
        ]
        st.markdown(f"**User:** {query}")
        st.markdown(f"**Assistant:** {answer}")
