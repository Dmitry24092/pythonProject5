from flask import Flask
from utils import *

app = Flask(__name__)

@app.route("/")
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route("/candidate/<int:pk>")
def page_candidate(pk):
    """Поиск кандидата по рк"""
    candidate: dict = get_candidate_by_id(pk)
    result: str = format_candidates([candidate])
    return result

app.run()