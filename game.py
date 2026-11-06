
import random
from datetime import datetime

from quiz import Quiz
from storage import load_state, save_state


DEFAULT_HINT = "정답을 고르기 전에 각 보기의 의미를 비교해 보세요."


class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz(
                "변수를 사용하는 주된 이유는?",
                ["프로그램을 종료하기 위해", "데이터를 저장하고 재사용하기 위해",
                 "오류를 삭제하기 위해", "파일을 복사하기 위해"],
                2,
                DEFAULT_HINT
            ),
            Quiz(
                "list와 dict의 차이로 올바른 것은?",
                ["둘 다 숫자만 저장한다", "list는 키와 값으로 저장한다",
                 "dict는 순서를 사용할 수 없다",
                 "list는 순서대로, dict는 키와 값으로 데이터를 관리한다"],
                4,
                DEFAULT_HINT
            ),
            Quiz(
                "여러 조건에 따라 다른 코드를 실행하는 구문은?",
                ["if/elif/else", "import", "class", "return"],
                1,
                DEFAULT_HINT
            ),
            Quiz(
                "for와 while의 차이로 올바른 것은?",
                ["for는 조건문이다", "while은 함수를 만든다",
                 "for는 항목을 순회하고 while은 조건이 참인 동안 반복한다",
                 "두 구문은 파일 저장에 사용한다"],
                3,
                DEFAULT_HINT
            ),
            Quiz(
                "클래스에서 __init__ 메서드의 주된 역할은?",
                ["프로그램 종료", "객체의 초기 상태 설정",
                 "파일 삭제", "GitHub 업로드"],
                2,
                DEFAULT_HINT
            ),
            Quiz(
                "인스턴스 메서드에서 self가 가리키는 것은?",
                ["현재 객체 자신", "모든 파이썬 파일",
                 "Git 저장소", "프로그램 사용자"],
                1,
                DEFAULT_HINT
            ),
            Quiz(
                "게임의 문제와 점수를 JSON으로 저장하는 이유는?",
                ["실행 속도를 무조건 높이기 위해", "이미지를 만들기 위해",
                 "Python을 설치하기 위해",
                 "구조화된 데이터를 파일에 기록하고 복원하기 위해"],
                4,
                DEFAULT_HINT
            ),
            Quiz(
                "프로그램 실행 중 발생하는 예외를 처리하는 구문은?",
                ["for/in", "try/except", "def/return", "if/elif"],
                2,
                DEFAULT_HINT
            ),
            Quiz(
                "git add와 git commit의 역할로 올바른 것은?",
                ["둘 다 저장소를 삭제한다",
                 "add는 업로드, commit은 다운로드한다",
                 "add는 변경을 등록하고 commit은 이력을 기록한다",
                 "둘 다 브랜치를 생성한다"],
                3,
                DEFAULT_HINT
            ),
            Quiz(
                "다른 브랜치의 변경 사항을 현재 브랜치에 병합하는 명령어는?",
                ["git clone", "git init", "git status", "git merge"],
                4,
                DEFAULT_HINT
            )
        ]

        self.high_score = 0
        self.history = []

        saved = load_state()

        if saved is not None:
            try:
                saved_quizzes = [
                    Quiz(
                        item["question"],
                        item["choices"],
                        item["answer"],
                        item.get("hint", DEFAULT_HINT)
                    )
                    for item in saved["quizzes"]
                ]

                self.quizzes = saved_quizzes
                self.high_score = saved["high_score"]
                self.history = saved.get("history", [])

            except (KeyError, TypeError, ValueError):
                print("경고: 저장 데이터 형식이 잘못되어 기본값을 사용합니다.")

    def play(self):
        print("\n=== 퀴즈 풀기 ===")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        quizzes_to_play = self.quizzes.copy()
        random.shuffle(quizzes_to_play)

        while True:
            count_text = input(
                f"몇 문제를 풀까요? (1~{len(quizzes_to_play)}): "
            ).strip()

            if not count_text.isdecimal():
                print("숫자를 입력해주세요.")
                continue

            count = int(count_text)

            if 1 <= count <= len(quizzes_to_play):
                break

            print(f"1~{len(quizzes_to_play)} 사이의 숫자를 입력해주세요.")

        quizzes_to_play = quizzes_to_play[:count]
        score = 0

        for number, quiz in enumerate(quizzes_to_play, start=1):
            print(f"\n문제 {number}/{len(quizzes_to_play)}")
            quiz.show()

            hint_used = False

            while True:
                answer_text = input(
                    "정답 번호 (1~4, 힌트 0): "
                ).strip()

                if answer_text == "0":
                    if quiz.hint:
                        quiz.show_hint()
                        hint_used = True
                    else:
                        print("이 문제에는 등록된 힌트가 없습니다.")
                    continue

                if not answer_text.isdecimal():
                    print("숫자를 입력해주세요.")
                    continue

                answer = int(answer_text)

                if not 1 <= answer <= 4:
                    print("1~4 사이의 번호를 입력해주세요.")
                    continue

                break

            if quiz.check_answer(answer):
                if hint_used:
                    score += 0.5
                    print("정답입니다! (힌트 사용: 0.5점)")
                else:
                    score += 1
                    print("정답입니다! (1점)")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        percentage = round(score / len(quizzes_to_play) * 100)

        print(
            f"\n최종 점수: {score}/{len(quizzes_to_play)} "
            f"({percentage}점 / 100점)"
        )

        if percentage > self.high_score:
            self.high_score = percentage
            print("새로운 최고 점수를 달성했습니다!")

        record = {
            "date": datetime.now().isoformat(timespec="seconds"),
            "question_count": len(quizzes_to_play),
            "score": score,
            "percentage": percentage
        }

        self.history.append(record)

        if not save_state(self.quizzes, self.high_score, self.history):
            self.history.pop()
            print("경고: 점수 및 히스토리 저장에 실패했습니다.")
        else:
            print("플레이 기록이 저장되었습니다.")

        return score

    def add_quiz(self):
        print("\n=== 새로운 퀴즈 추가 ===")

        while True:
            question = input("문제 내용을 입력하세요: ").strip()
            if question:
                break
            print("문제 내용을 입력해주세요.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 보기: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("보기 내용을 입력해주세요.")

        while True:
            answer_text = input("정답 번호 (1~4): ").strip()

            if not answer_text.isdecimal():
                print("숫자를 입력해주세요.")
                continue

            answer = int(answer_text)

            if 1 <= answer <= 4:
                break

            print("1~4 사이의 번호를 입력해주세요.")

        new_quiz = Quiz(question, choices, answer, DEFAULT_HINT)
        self.quizzes.append(new_quiz)

        if save_state(self.quizzes, self.high_score, self.history):
            print("새로운 퀴즈가 추가되고 저장됐습니다!")
        else:
            self.quizzes.pop()
            print("파일 저장에 실패하여 퀴즈 추가를 취소했습니다.")

    def list_quizzes(self):
        print("\n=== 등록된 퀴즈 목록 ===")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

        print(f"\n전체 문제 수: {len(self.quizzes)}")

    def delete_quiz(self):
        print("\n=== 퀴즈 삭제 ===")

        if len(self.quizzes) <= 5:
            print("최소 5문제는 유지해야 하므로 삭제할 수 없습니다.")
            return

        self.list_quizzes()

        while True:
            number_text = input("\n삭제할 문제 번호 (취소 0): ").strip()

            if number_text == "0":
                print("삭제를 취소했습니다.")
                return

            if not number_text.isdecimal():
                print("숫자를 입력해주세요.")
                continue

            number = int(number_text)

            if 1 <= number <= len(self.quizzes):
                break

            print("목록에 있는 문제 번호를 입력해주세요.")

        selected_quiz = self.quizzes[number - 1]
        print(f"\n선택한 문제: {selected_quiz.question}")

        confirm = input("정말 삭제하시겠습니까? (y/n): ").strip().lower()

        if confirm != "y":
            print("삭제를 취소했습니다.")
            return

        removed_quiz = self.quizzes.pop(number - 1)

        if save_state(self.quizzes, self.high_score, self.history):
            print("퀴즈가 삭제되었습니다.")
            print(f"남은 문제 수: {len(self.quizzes)}")
        else:
            self.quizzes.insert(number - 1, removed_quiz)
            print("파일 저장에 실패하여 삭제를 취소했습니다.")

    def show_score(self):
        print("\n=== 최고 점수 확인 ===")

        if not self.history and self.high_score == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"현재 최고 점수: {self.high_score}점 / 100점")

    def show_history(self):
        print("\n=== 점수 히스토리 ===")

        if not self.history:
            print("아직 저장된 플레이 기록이 없습니다.")
            return

        for number, record in enumerate(self.history, start=1):
            print(
                f"{number}. {record['date']} | "
                f"{record['question_count']}문제 | "
                f"{record['score']}점 | "
                f"100점 만점 기준 {record['percentage']}점"
            )
