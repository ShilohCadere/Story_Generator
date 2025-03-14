from flask import Flask, render_template, request
import random
    
app = Flask(__name__)
    
story_parts = {
    "character": ["wizard", "knight", "princess", "dragon"],
    "setting": ["forest", "castle", "mountain", "cave"],
    "problem": ["lost their way", "was captured", "needed help", "guarded a treasure"],
    "solution": ["found a map", "was rescued", "helped them", "outsmarted them"]
}
    
def generate_story():
    story = ""
    for part, options in story_parts.items():
        story += random.choice(options) + " "
    return story
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        story = generate_story()
        return render_template("index.html", story=story)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)