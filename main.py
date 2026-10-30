from game import QuizGame


def main():
    game = QuizGame()

    while True:
        print("\n================================")
        print("       Python & Git 기초 학습 퀴즈")
        print("================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("================================")

        try:
            choice = input("메뉴 선택 (1~5): ").strip()

            if choice == "1":
                game.play()
            elif choice == "2":
                game.add_quiz()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            elif choice == "3":
                game.list_quizzes()
            elif choice == "4":
                game.show_score()
            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 종료되어 프로그램을 마칩니다.")
            break


if __name__ == "__main__":
    main()
