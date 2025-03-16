from flask import Flask, render_template, request, redirect, url_for
import openai

openai.api_key = 'Your Secret Key'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    story = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        story = generate_story(prompt)
    return render_template('index.html', story=story)


def generate_story(prompt):
    try:
        # Call the OpenAI API
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",  # You can use other models as well
            prompt=prompt,
            max_tokens=500,  # Adjust the length of the story
            temperature=0.7,  # Adjust for creativity/randomness
        )
        # Extract story text from response
        story = response.choices[0].text.strip()
        return story
    except Exception as e:
        return f"Error generating story: {e}"
    
if __name__ == '__main__':
    app.run(debug=True)