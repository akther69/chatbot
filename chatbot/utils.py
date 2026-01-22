import re
from difflib import get_close_matches
from .models import ChatPattern

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)  # remove symbols like ? ! .
    return text

def get_bot_response(user_message):
    user_message = clean_text(user_message)

    patterns = ChatPattern.objects.all()
    questions = [clean_text(p.question) for p in patterns]

    match = get_close_matches(user_message, questions, n=1, cutoff=0.4)

    if match:
        best_question = match[0]
        for p in patterns:
            if clean_text(p.question) == best_question:
                return p.answer

    return "Sorry, I didn’t understand that. Can you rephrase?"
