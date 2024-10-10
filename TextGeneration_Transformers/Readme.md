# Text Generation using GPT-2

This project demonstrates how to generate text using the GPT-2 model from the Hugging Face Transformers library. The model is fine-tuned to continue a given seed text and produce human-like text output.

## Project Overview

The project uses the GPT-2 language model to generate text based on a given prompt (`seed_text`). The Hugging Face `transformers` package is used to load the pre-trained GPT-2 model and tokenizer. Parameters such as the maximum length of the generated text, temperature, and prevention of repetitive sequences are configurable.

### Features:
- **Pre-trained GPT-2 Model:** Uses the powerful GPT-2 model from Hugging Face.
- **Text Generation Control:** Set maximum text length, control temperature for creativity, and avoid repeated n-grams.
- **Customizable Prompt:** Input a seed text to start the text generation.

## Installation

To run this project, you need to have Python installed along with the required dependencies. You can install the necessary packages using pip:

```bash
pip install torch transformers
