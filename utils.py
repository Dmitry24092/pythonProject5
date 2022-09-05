import json


def load_json() -> list[dict]:
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates

def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = "<pre>"

    for candidate in candidates:
        result += f"""
              {candidate["name"]}\n
              {candidate["position"]}\n
              {candidate["skills"]}\n
          """
    result += "<pre>"
    return result

def get_all_candidates() -> list[dict]:
    return load_json()

def get_candidate_by_id(pk: int) ->dict:
    candidates = get_all_candidates
    for candidate in candidates:
        if candidate["pk"] == "pk":
            return candidate
    return "Not found"


