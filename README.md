# Qdoc - AI-powered Article Assistant

Qdoc is a Flask web application that utilizes a Large Language Model (LLM) to summarize articles from a given URL or PDF. Additionally, it can answer questions related to the article using the conversation history, the article's content, and common knowledge.

## Purpose

The purpose of Qdoc is to make information consumption more efficient and interactive. It seamlessly integrates with articles through URL or PDF inputs, offering summarized content and the ability to engage in a dynamic question-answering conversation. It is designed to be practical, user-friendly, and a valuable tool for anyone dealing with information-rich documents. Whether it is a lengthy article or a complex research paper, Qdoc can help with quickly understanding and interacting with the content.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [Note](#note)

## Features
- **Summarization from URL or PDF:** Summarize the contents of an article by providing a URL or PDF link.
- **Question-Answering:** Inquire about specific details or seek clarification regarding the article, and the system generates answers based on conversation history and article content.
- **Conversation History:** Ask follow-up questions based on the ongoing conversation.
- **Refresh Conversation:** Clear the conversation history to initiate a fresh dialogue.

## Prerequisites
- Python 3.x
- [OpenAI API Key](https://beta.openai.com/signup/)
- Dependencies listed in the `requirements.txt` file.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/lancerai/Qdoc.git
    cd Qdoc
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your OpenAI API key by adding it to the `.env` file:
    ```dotenv
    OPENAI_API_KEY=your-api-key-here
    ```
4. Run the application:
    ```bash
    python qdoc.py
    ```

## Usage
1. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.
2. Summarize an article by providing the URL or PDF.
3. Ask questions about the article to receive insightful answers. Qdoc will dynamically adapt to the ongoing dialogue.
4. Click "Refresh" to clear the conversation history and start a new interaction.

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## Note

Make sure to comply with OpenAI's use-case policies and guidelines when using this app.

### Enjoy using Qdoc, your intelligent companion for exploring articles effortlessly!
