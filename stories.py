"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.get_result_text(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def get_result_text(self, answers):
        """Return result text from dictionary of {prompt: answer, ...}."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """ I like to go eat at {place}, and I always {adjective} {noun}.
    But I had to {verb} in order to hangout with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

fun_story = Story(
    ["adjective", "plural_noun"],
    """I have never slept on top of some {plural_noun} but I believe
     that would be very {adjective}!"""
)

scary_story = Story(
    ["verb", "adjective", "noun"],
    """There is a scary house I always {verb} and when I am {adjective}
    I tend to grab my friend's {noun}"""
)

story_collection = [scary_story, fun_story, excited_story, silly_story]
