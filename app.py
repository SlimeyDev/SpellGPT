from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

@app.route("/")
def home():
    #home
    return render_template("spellGPT.html")

@app.route("/process", methods=["POST", "GET"])
def process():
    #gathering text and mode
    text = request.form["text"]
    mode = request.form["modes"]
    #checking if text is entered or not
    if text.isspace() or text == "":
        return render_template("spellGPT.html", text="ERROR: No text provided")
    key = os.getenv("OPEN_AI")
    # processing the text
    if mode == "SnG":
        prompt = "correct the grammar and spelling in this text and only return the corrected text only:" + text
    elif mode == "formal":
        prompt = "change the tone of this text to formal without compromising its meaning and only return the new text only: " + text
    elif mode == "informal":
        prompt = "change the tone of this text to informal without compromising its meaning and only return the new text only: " + text
    elif mode == "casual":
        prompt = "change the tone of this text to casual without compromising its meaning and only return the new text only: " + text
    elif mode == "shakespeare":
        prompt = "Change the way this text has been written to the way shakespeare would have written it and only return the new text only: " + text
    elif mode == "GenZ":
        prompt = "Change the way this text has been written to the way a GenZ would have written it and only return the new text only: " + text
    else:
        processed_text = "An unknown error occurred!"
        return render_template("spellGPT.html", text=processed_text, mode=mode)

    openai.api_key = key
    messages = []
    system_msg = "chat"
    messages.append({"role": "system", "content": system_msg})
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    processed_text = reply
    
    return render_template("spellGPT.html", text=processed_text, mode=mode)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)