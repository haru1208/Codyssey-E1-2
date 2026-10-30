from game import QuizGame


def main():
    game = QuizGame()

    while True:
        print("\n================================")
        print("       나만의 파이썬 퀴즈 게임")
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
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            elif choice in ("2", "3", "4"):
                print("해당 기능은 다음 단계에서 구현합니다.")
            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 종료되어 프로그램을 마칩니다.")
            break


if __name__ == "__main__":
    main()
