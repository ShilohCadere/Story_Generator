from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

generator = pipeline('text-generation', model='gpt2')
@app.route('/', methods=['GET', 'POST'])
def index():
    story = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        story = generator(prompt, max_length=2000, num_return_sequences=1)[0]['generated_text']
    return render_template('index.html', story=story)

    
if __name__ == '__main__':
    app.run(debug=True)