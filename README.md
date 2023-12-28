# Qdoc: Your Intelligent Article Assistant

Qdoc is an intelligent article assistant powered by a Large Language Model (LLM). It enhances your experience with articles by providing summarization and question-answering capabilities. Whether you have a lengthy article or a complex research paper, Qdoc helps you quickly understand and interact with the content.

## Purpose

The purpose of Qdoc is to make information consumption more efficient and interactive. It seamlessly integrates with articles through URL or PDF inputs, offering summarized content and the ability to engage in a dynamic question-answering conversation. Qdoc is designed to be practical, user-friendly, and a valuable tool for anyone dealing with information-rich documents.

## Features

### 1. Summarization from URL or PDF

- **Input Flexibility:** Enter the URL of an online article or a link to a PDF document.
- **Content Summarization:** Receive a concise and easily understandable summary of the article.

### 2. Dynamic Question-Answering

- **Ask Questions:** Inquire about specific details or seek clarification regarding the article.
- **Context-Aware Responses:** Qdoc maintains a conversation history to provide context-aware answers.

### 3. Conversation History

- **Follow-Up Queries:** Seamlessly ask follow-up questions based on the ongoing conversation.
- **Visualize History:** The conversation history is displayed, allowing you to track interactions.

### 4. Refresh Conversation

- **Start Anew:** Clear the conversation history to initiate a fresh dialogue.

## Setup

### 1. Clone the Repository:

- git clone https://github.com/lancerai/Qdoc.git
- cd Qdoc


### 2. Install Dependencies:

- pip install -r requirements.txt

### 3. Set Up OpenAI API Key:
Create a .env file in the project root and add your OpenAI API key:

- OPENAI_API_KEY=your-api-key

### 4. Run the Application:

- python qdoc.py

## Usage

### 1. Access Qdoc:

- Open your browser and go to http://127.0.0.1:5000/.

### 2. Summarize an Article:

- Enter the article URL or PDF link in the respective form.
- Click "Summarize" to receive a summary of the content.

### 3. Engage in Q&A:

- Ask questions about the article, and receive insightful answers.
- The conversation history is displayed, allowing for context-aware interactions.

### 4. Follow-Up Queries:

- Continue the conversation with follow-up questions.
- Qdoc dynamically adapts to the ongoing dialogue.

### 5. Refresh Conversation:

- Click "Refresh" to clear the conversation history and start a new interaction.

### Additional Information

- Qdoc uses OpenAI's Chat API for language model interactions.
- Handle API rate limits based on your OpenAI subscription.

Enjoy using Qdoc, your intelligent companion for exploring articles effortlessly!

# Qdoc

Qdoc is a project that utilizes a Language Model (LM) to summarize articles based on relevant aggregated content from a given URL or PDF. Additionally, it can answer questions related to the article using conversation history, the article's content, and common knowledge.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Summarization from URL or PDF:** Summarize the content of articles using a provided URL or PDF file.
- **Question-Answering:** Ask questions related to the article, and the system generates answers based on conversation history and article content.
- **Conversation History:** Maintain a conversation history to improve context-aware question-answering.

## Prerequisites
- Python 3.x
- [OpenAI API Key](https://beta.openai.com/signup/)
- Dependencies listed in the `requirements.txt` file.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Qdoc.git
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
3. Ask questions about the article to receive context-aware answers.

## Examples
### Summarize an Article
- Provide the article URL or PDF.
![Summarize Example](images/summarize-example.png)

### Ask Questions
- Enter your question and the article URL to receive answers.
![Query Example](images/query-example.png)

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
