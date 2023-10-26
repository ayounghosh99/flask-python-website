import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import openai

app = Flask(__name__)
CORS(app, resources={r"/generate_text": {"origins": "http://localhost:3000"}})

# Setting the OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     return f'Hello, {name}!'
    # return render_template('form.html')
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
@cross_origin()
def generate_text():
    prompt = request.json['prompt']

    # Making a request to the OpenAi API
    response = openai.Completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        max_tokens = 150
    )

    generated_text = response['choices'][0]['text']

    # return render_template('result.html', generated_text=generated_text)

    return jsonify({'generated_text' : generated_text})


if __name__ == '__main__':
    app.run(debug=True)


