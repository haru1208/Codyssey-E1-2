class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def show(self):
        print(f"\n{self.question}")

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, selected):
        return selected == self.answer

    def show_hint(self):
        if self.hint:
            print(f"\n힌트: {self.hint}")
        else:
            print("\n이 문제에는 등록된 힌트가 없습니다.")