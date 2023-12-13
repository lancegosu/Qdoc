from flask import Flask, render_template, request, jsonify
from utils import summarize_from_url, get_article_text, summarize_from_pdf, generate_answer

app = Flask(__name__)

conversation_history = [] # Initialize conversation history as a global variable

@app.route('/')
def home():
    return render_template('index.html') # Render the home page using the 'index.html' template
    
@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['user_input2'] # Get the article URL from the form data
    
    # Check if the URL ends with ".pdf" to determine if it's a PDF file
    if url.endswith(".pdf"):
        result = summarize_from_pdf(url)
    else:
        result = summarize_from_url(url)
    return result

@app.route('/query', methods=['POST'])
def query():
    global conversation_history
    user_question = request.form['user_input3']  # Get the user's question from the form
    article_url = request.form['user_input2']  # Get the article URL from the form
    conversation_history.append({"role": "user", "message": user_question}) # Add the user's question to the conversation history
    article_text = get_article_text(article_url) # Get the text of the article from the provided URL

    # Check if article text retrieval was successful
    if article_text is None:
        return "Failed to retrieve article text."

    answer = generate_answer(user_question, article_text, conversation_history) # Generate an answer using the user's question, article text, and conversation history
    conversation_history.append({"role": "system", "message": answer}) # Add the system's answer to the conversation history

    return jsonify(conversation_history) # Return the conversation history as a JSON response

@app.route('/refresh', methods=['POST'])
def refresh():
    global conversation_history
    conversation_history.clear() # Clear the conversation history
    return ('', 204)  # Return an empty response with a status code 204 (No Content)

if __name__ == '__main__':
    app.run()
