from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz(
                "파이썬 파일의 확장자는?",
                [".txt", ".py", ".jpg", ".html"],
                2
            ),
            Quiz(
                "화면에 글자를 출력하는 함수는?",
                ["input()", "print()", "len()", "type()"],
                2
            ),
            Quiz(
                "파이썬에서 주석을 시작하는 기호는?",
                ["@", "#", "$", "&"],
                2
            ),
            Quiz(
                "여러 값을 순서대로 저장하는 자료형은?",
                ["str", "int", "list", "bool"],
                3
            ),
            Quiz(
                "len('cat')의 실행 결과는?",
                ["2", "3", "4", "5"],
                2
            )
        ]

    def play(self):
        score = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {number}/{len(self.quizzes)}")
            quiz.show()

            while True:
                answer_text = input("정답 번호 (1~4): ").strip()

                if not answer_text.isdecimal():
                    print("숫자를 입력해주세요.")
                    continue

                answer = int(answer_text)

                if answer < 1 or answer > 4:
                    print("1~4 사이의 번호를 입력해주세요.")
                    continue

                break

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n최종 점수: {score}/{len(self.quizzes)}")
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

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("새로운 퀴즈가 추가됐습니다!")
