from flask import Flask, render_template, request, jsonify
import requests  # Pour appeler l'API Mistral

app = Flask(__name__)

# Remplace par ta clé API Mistral (ou autre)
API_KEY = "WCTIoWiG8Uw5gRb3zIzconuTL5KXZyGS"
API_URL = "https://api.mistral.ai/v1/chat/completions"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_ia():
    user_message = request.json["message"]

    # Appel à l'API Mistral
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    ia_reply = response.json()["choices"][0]["message"]["content"]

    return jsonify({"reply": ia_reply})

if __name__ == "__main__":
    app.run(debug=True)
