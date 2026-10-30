import json
from pathlib import Path


STATE_FILE = Path(__file__).with_name("state.json")


def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return None

    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"경고: 저장 파일을 읽지 못했습니다: {error}")
        return None


def save_state(quizzes, high_score):
    data = {
        "quizzes": [
            {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            }
            for quiz in quizzes
        ],
        "high_score": high_score
    }

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True

    except (OSError, UnicodeError, TypeError) as error:
        print(f"경고: 저장하지 못했습니다: {error}")
        return False
