from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, scary_story, fun_story, excited_story, story_collection

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/questions')
def questions():
    """input form for story, renders form"""
    ###
    website_prompts = story_collection[int(request.args.get('a'))].prompts
    index_item = int(request.args.get('a'))
    return render_template(
        'questions.html',
        index_item=index_item,
        website_prompts=website_prompts
    )


@app.get("/results")
def result_page():
    """displays the result"""
    created_story = story_collection[int(
        request.args.get('a'))].get_result_text

    return render_template(
        'results.html',
        created_story=created_story
    )


@app.get('/')
def home_page():
    """homepage for madlibs website."""
    return render_template('stories.html')
