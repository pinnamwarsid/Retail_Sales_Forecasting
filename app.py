from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# FastAPI Chatbot URL
CHATBOT_API_URL = "http://127.0.0.1:8000/chat"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Send the message to the FastAPI chatbot
    response = requests.post(CHATBOT_API_URL, json={"message": user_message})
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"response": "Error communicating with chatbot!"})

if __name__ == "__main__":
    app.run(debug=True)

