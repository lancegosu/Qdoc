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



## Setup

### 1. **Clone the Repository:**

- git clone https://github.com/lancerai/Qdoc.git
- cd Qdoc


### 2. **Install Dependencies:**

- pip install -r requirements.txt

### 3. **Set Up OpenAI API Key:**
Create a .env file in the project root and add your OpenAI API key:

- OPENAI_API_KEY=your-api-key

### 4. **Run the Application:**

- python qdoc.py

## Usage

### 1. **Access Qdoc:**

- Open your browser and go to http://127.0.0.1:5000/.

### 2. **Summarize an Article:**

- Enter the article URL or PDF link in the respective form.
- Click "Summarize" to receive a summary of the content.

### 3. **Engage in Q&A:**

- Ask questions about the article, and receive insightful answers.
- The conversation history is displayed, allowing for context-aware interactions.

### 4. Follow-Up Queries:

- Continue the conversation with follow-up questions.
- Qdoc dynamically adapts to the ongoing dialogue.

### Additional Information

- Qdoc uses OpenAI's Chat API for language model interactions.
- Handle API rate limits based on your OpenAI subscription.


Enjoy using Qdoc, your intelligent companion for exploring articles effortlessly!
