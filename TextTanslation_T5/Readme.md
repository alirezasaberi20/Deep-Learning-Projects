# Text Translation using T5 Transformer

This project demonstrates how to perform text translation using the T5 model from the Hugging Face Transformers library. The model translates a given input text from English to French using a pre-trained T5 model.

## Project Overview

The project utilizes the T5 (Text-To-Text Transfer Transformer) model to translate text between languages. The pre-trained T5 model is used with the Hugging Face `transformers` package to perform translation tasks efficiently. This example focuses on translating text from English to French.

### Features:
- **Pre-trained T5 Model:** Uses the `t5-small` model from Hugging Face.
- **Text Translation:** Translate any English sentence into French by modifying the input prompt.
- **Customizable Translation:** The project supports customizing the source and target languages by modifying the input prompt.

## Installation

To get started, you'll need to install the necessary dependencies. You can install them using pip:

```bash
pip install torch transformers
