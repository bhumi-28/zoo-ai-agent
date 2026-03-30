from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if "hello" in user_message.lower():
        reply = "Hi there 👋"
    elif "zoo" in user_message.lower():
        reply = "Welcome to Zoo AI 🐼"
    else:
        reply = "I am your Zoo AI Agent 🤖"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
