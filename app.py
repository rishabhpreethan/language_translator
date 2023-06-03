from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    destination_lang = request.form['destination_lang']

    response = requests.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={destination_lang}&dt=t&q={text}")
    translated_text = response.json()[0][0][0]

    return render_template('result.html', text=text, translated_text=translated_text)

if __name__ == '__main__':
    app.run()
