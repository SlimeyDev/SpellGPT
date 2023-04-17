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
        key = os.getenv("OPEN_AI")
        if mode == "SnG":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "correct the grammar and spelling in this text and only return the corrected text only:"+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("SnG")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "formal":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to formal without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("formal")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "informal":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to informal without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("informal")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "casual":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to casual without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("casual")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "shakespeare":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "Change the way this text has been written to the way shakespeare would have written it and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("shakespeare")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "GenZ":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "Change the way this text has been written to the way a GenZ would have written it and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("GenZ")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "Optimistic":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to optimistic without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("Optimistic")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "Worried":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to worried without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("Worried")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "Friendly":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to friendly without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("Friendly")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "Cooperative":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to cooperative without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("Friendly")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)
        elif mode == "Surprised":
            openai.api_key = key
            messages = []
            system_msg = "chat"
            messages.append({"role": "system", "content": system_msg})
            messages.append({"role": "user", "content": "change the tone of this text to surprised without compromising its meaning and only return the new text only: "+text})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("Friendly")
            print(reply)
            processed_text = reply
            return render_template("spellGPT.html", text=processed_text, mode=mode)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)