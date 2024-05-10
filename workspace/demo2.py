# じゃんけんゲームを書いてください
import random
import unittest

# 勝敗の判定ロジックをハンドルするjudge関数を定義
def judge(user_hand, computer_hand):
    #プレイヤーの手とコンピューターの手を比較して結果を表示
    if user_hand == computer_hand:
        return "あいこです"
    elif (user_hand == "グー" and computer_hand == "チョキ") or (user_hand == "チョキ" and computer_hand == "パー") or (user_hand == "パー" and computer_hand == "グー"):
        return "勝ちです"
    else:
        return "負けです"

# judge関数を使ってじゃんけんをするmain関数を定義
def main():
    print("じゃんけんゲームを始めます")
    while True:
        # ユーザーの手を入力
        user_hand = input("じゃんけんの手を入力してください: ")
        # 入力が空の場合はもう一度入力してもらう
        if user_hand == "":
            print("じゃんけんの手を入力してください")
            continue
        # 入力が数字の場合は文字列に変換
        if user_hand.isdigit():
            user_hand = int(user_hand)
        # 入力が前後にスペースが入っている場合は削除
        user_hand = user_hand.strip()
        # 入力が大文字の場合は小文字に変換
        user_hand = user_hand.lower()
        # 入力がグー、チョキ、パー以外の場合はもう一度入力してもらう
        if user_hand not in ["グー", "チョキ", "パー"]:
            print("グー、チョキ、パーのいずれかを入力してください")
            continue
        # コンピュータの手をランダムで決定
        computer_hand = random.choice(["グー", "チョキ", "パー"])
        # じゃんけんの結果を判定
        result = judge(user_hand, computer_hand)
        print(result)
        # もう一度じゃんけんを続けるかどうかを入力
        is_continue = input("もう一度じゃんけんを続けますか？(y/n): ")
        # 入力が空の場合はもう一度入力してもらう
        if is_continue == "":
            print("yかnを入力してください")
            continue
        # 入力が大文字の場合は小文字に変換
        is_continue = is_continue.lower()
        # 入力がyの場合はじゃんけんを続ける
        if is_continue == "y":
            continue
        # 入力がnの場合はじゃんけんを終了する
        elif is_continue == "n":
            print("じゃんけんゲームを終了します")
            break
        # 入力がyでもnでもない場合はもう一度入力してもらう
        else:
            print("yかnを入力してください")
            continue

    # ９通りのテストケースを作成
class TestJudge(unittest.TestCase):
    #グーをテスト
    def test_gu(self):
        self.assertEqual(judge("グー", "グー"), "あいこです")
        self.assertEqual(judge("グー", "チョキ"), "勝ちです")
        self.assertEqual(judge("グー", "パー"), "負けです")
    #チョキをテスト
    def test_choki(self):
        self.assertEqual(judge("チョキ", "グー"), "負けです")
        self.assertEqual(judge("チョキ", "チョキ"), "あいこです")
        self.assertEqual(judge("チョキ", "パー"), "勝ちです")
    #パーをテスト
    def test_pa(self):
        self.assertEqual(judge("パー", "グー"), "勝ちです")
        self.assertEqual(judge("パー", "チョキ"), "負けです")
        self.assertEqual(judge("パー", "パー"), "あいこです")

# テストを実行
if __name__ == "__main__":
    unittest.main()
