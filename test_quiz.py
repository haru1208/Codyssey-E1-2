import unittest
from quiz import Quiz


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz(
            "파이썬 파일의 확장자는 무엇일까요?",
            [".txt", ".py", ".jpg", ".html"],
            2
        )

    def test_quiz_data(self):
        self.assertEqual(len(self.quiz.choices), 4)
        self.assertEqual(self.quiz.answer, 2)

    def test_correct_answer(self):
        self.assertTrue(self.quiz.check_answer(2))

    def test_wrong_answer(self):
        self.assertFalse(self.quiz.check_answer(1))


if __name__ == "__main__":
    unittest.main()