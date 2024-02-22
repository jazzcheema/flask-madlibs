from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def homepage():
    """homepage for madlibs website."""
    website_prompts = silly_story.prompts

    return render_template(
        'questions.html',
        website_prompts = website_prompts
        )

