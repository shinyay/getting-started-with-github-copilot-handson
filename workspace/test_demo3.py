import unittest
from demo3 import judge

class TestJankenGame(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(judge("グー", "グー"), "あいこです")
        self.assertEqual(judge("チョキ", "チョキ"), "あいこです")
        self.assertEqual(judge("パー", "パー"), "あいこです")

    def test_user_win(self):
        self.assertEqual(judge("グー", "チョキ"), "勝ちです")
        self.assertEqual(judge("チョキ", "パー"), "勝ちです")
        self.assertEqual(judge("パー", "グー"), "勝ちです")

    def test_user_lose(self):
        self.assertEqual(judge("グー", "パー"), "負けです")
        self.assertEqual(judge("チョキ", "グー"), "負けです")
        self.assertEqual(judge("パー", "チョキ"), "負けです")

if __name__ == "__main__":
    unittest.main()
