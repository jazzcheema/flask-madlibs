from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

#renders form in docstring
@app.get('/')
def home_page():
    """homepage for madlibs website."""
    website_prompts = silly_story.prompts

    return render_template(
        'questions.html',
        website_prompts = website_prompts
        )

@app.get("/results")
def result_page():
    """displays the result"""
    created_story = silly_story.get_result_text(request.args)

    return render_template(
        'results.html',
        created_story = created_story
    )

