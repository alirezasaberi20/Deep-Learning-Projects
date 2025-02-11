
# Chat with Your Document

This project is a **Streamlit application** that allows users to upload a PDF file and chat with its contents using a **Retrieval-Augmented Generation (RAG)** approach. The application processes the PDF file by splitting it into manageable chunks, indexing these chunks with a **vector store**, and then retrieving relevant information in response to user queries. It also maintains a conversation history that is displayed in the user interface.

## Features

- **User-Friendly PDF Upload**  
  Users can easily upload a PDF file via drag-and-drop or file selection.

- **Document Processing**  
  The PDF is loaded using LangChain’s `PyPDFLoader` and split into chunks using `RecursiveCharacterTextSplitter`.

- **Vector Indexing & Retrieval**  
  Chunks are indexed using a **Chroma vector store** with embeddings from `GoogleGenerativeAIEmbeddings`. The retrieval process uses **similarity search** to find relevant text segments.

- **Conversational Interface**  
  A **conversational retrieval chain** (powered by `ChatGoogleGenerativeAI` and enhanced with `ConversationBufferMemory`) answers user queries using both the current query and the entire chat history.

- **Chat History Display**  
  All previous user and assistant messages are stored in the session state and displayed on the interface.

## Installation

### Prerequisites

- **Python 3.10+**
- **Streamlit**
- Required Python packages (install via `pip`):

  ```bash
  pip install streamlit langchain-community langchain_google_genai langchain_chroma python-dotenv
