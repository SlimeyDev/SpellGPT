from flask import Flask, request, render_template
import openai

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
    if text == "Paste your text here!" or text.isspace() or text == "":
        return render_template("spellGPT.html", text="ERROR: No text provided")
    else:
        #outputting the processed text
        key = str("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")
        openai.api_key = key
        messages = []
        system_msg = "chat"
        messages.append({"role": "system", "content": system_msg})
        messages.append({"role": "user", "content": "correct the grammar in this text and only return the corrected text:"+text})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print(reply)
        processed_text = reply
        return render_template("spellGPT.html", text=processed_text, mode=mode)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)