from flask import Flask, render_template, request
    
app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    story_input = request.form['story_input']
    # Process the input (e.g., add to the story)
    updated_story = f"Once upon a time, there was a person named {name}. {story_input}"
    return render_template('result.html', story=updated_story)
    
if __name__ == '__main__':
    app.run(debug=True)