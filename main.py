
from game import QuizGame
from storage import save_state


def main():
    game = QuizGame()

    try:
        while True:
            print("\n================================")
            print("       Python & Git 기초 학습 퀴즈")
            print("================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("6. 퀴즈 삭제")
            print("7. 점수 히스토리")
            print("================================")

            choice = input("메뉴 선택 (1~7): ").strip()

            if choice == "1":
                game.play()
            elif choice == "2":
                game.add_quiz()
            elif choice == "3":
                game.list_quizzes()
            elif choice == "4":
                game.show_score()
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            elif choice == "6":
                game.delete_quiz()
            elif choice == "7":
                game.show_history()
            else:
                print("잘못된 입력입니다. 1~7 사이의 숫자를 입력하세요.")

    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 안전하게 종료합니다.")

    finally:
        if save_state(game.quizzes, game.high_score, game.history):
            print("퀴즈 데이터와 완료된 플레이 기록을 저장했습니다.")
        else:
            print("경고: 데이터 저장에 실패했습니다.")


if __name__ == "__main__":
    main()
