from flask import Flask, request, jsonify, render_template
import re
import google.generativeai as genai

app = Flask(__name__)

# Configure the Gemini AI
genai.configure(api_key='AIzaSyAO36_LDr2H1jojusoSo72mscY6lA6BQO4')
model = genai.GenerativeModel('gemini-pro')

responses = {
    # Add specific patterns and responses for common queries
    r"\bavailability of beds\b": "The current bed availability status is being fetched. Please wait...",
    r"\badmission process\b": "To admit a patient, please ensure you have all required documents and visit the nearest OPD.",
    r"\bOPD queue status\b": "The OPD queue status is being fetched. Please hold on...",
}

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I'm sorry, I couldn't get an answer from Gemini. Error: {str(e)}"

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
    
    # If no predefined response is found, use Gemini (Avartan)
    gemini_prompt = f"""As an AI assistant for a hospital-based solution in India, 
    please provide a concise and accurate answer to the following question:
    {user_input}
    Focus on queuing models in OPDs, availability of beds, and patient admission procedures."""
    
    gemini_response = get_gemini_response(gemini_prompt)
    return f"I don't have an immediate answer for that, but for urgent medical support or detailed assistance, please contact your nearest healthcare provider or visit the hospital directly:\n{gemini_response}"

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/chat_window')
def chat_window():
    return render_template('chat_window.html')

@app.route('/')
def home():
    return render_template('chat_window.html')

if __name__ == '__main__':
    app.run(debug=True)
