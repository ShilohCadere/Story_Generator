from flask import Flask, render_template, request, redirect, url_for
import openai

openai.api_key = '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'

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