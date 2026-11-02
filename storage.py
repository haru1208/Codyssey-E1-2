
import json
from pathlib import Path


STATE_FILE = Path(__file__).with_name("state.json")


def is_valid_state(data):
    if not isinstance(data, dict):
        return False

    quizzes = data.get("quizzes")
    high_score = data.get("high_score")
    history = data.get("history", [])

    if not isinstance(quizzes, list) or not quizzes:
        return False

    if type(high_score) is not int or not 0 <= high_score <= 100:
        return False

    if not isinstance(history, list):
        return False

    for item in quizzes:
        if not isinstance(item, dict):
            return False

        question = item.get("question")
        choices = item.get("choices")
        answer = item.get("answer")
        hint = item.get("hint", "")

        if not isinstance(question, str) or not question.strip():
            return False

        if not isinstance(choices, list) or len(choices) != 4:
            return False

        if not all(isinstance(c, str) and c.strip() for c in choices):
            return False

        if type(answer) is not int or answer not in (1, 2, 3, 4):
            return False

        if not isinstance(hint, str):
            return False

    for record in history:
        if not isinstance(record, dict):
            return False

        if not isinstance(record.get("date"), str):
            return False

        count = record.get("question_count")
        score = record.get("score")
        percentage = record.get("percentage")

        if type(count) is not int or count < 1:
            return False

        if type(score) not in (int, float) or not 0 <= score <= count:
            return False

        if type(percentage) is not int or not 0 <= percentage <= 100:
            return False

    return True


def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if is_valid_state(data):
            return data

        print("경고: 저장 데이터가 올바르지 않아 기본값을 사용합니다.")
        return None

    except FileNotFoundError:
        return None

    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"경고: 저장 파일을 읽지 못했습니다: {error}")
        return None


def save_state(quizzes, high_score, history=None):
    if history is None:
        saved = load_state()
        history = saved.get("history", []) if saved else []

    data = {
        "quizzes": [
            {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "hint": quiz.hint
            }
            for quiz in quizzes
        ],
        "high_score": high_score,
        "history": history
    }

    if not is_valid_state(data):
        print("경고: 저장할 데이터 형식이 올바르지 않습니다.")
        return False

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True

    except (OSError, UnicodeError, TypeError) as error:
        print(f"경고: 저장하지 못했습니다: {error}")
        return False
