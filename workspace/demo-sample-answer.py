# じゃんけんゲームを書いてください
# じゃんけんの手は、グー、チョキ、パーのいずれかを入力してもらい、
# コンピュータと対戦してください
# じゃんけんの結果は、勝ち、負け、あいこのいずれかを表示してください
# じゃんけんを続けるかどうかは、ユーザーに入力してもらい、
# 続ける場合はじゃんけんを続け、終了する場合は終了してください
# じゃんけんの手は、グー、チョキ、パー以外のものを入力された場合は
# もう一度入力してもらってください
# じゃんけんの手を入力する際は、数字でも文字列でも入力できるようにしてください
# じゃんけんの手を入力する際は、大文字でも小文字でも入力できるようにしてください
# じゃんけんの手を入力する際は、前後にスペースが入っていても大丈夫なようにしてください
# じゃんけんの手を入力する際は、入力が空の場合はもう一度入力してもらってください

import random

# ロジックを全てハンドルするmain関数を定義
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
        if user_hand == computer_hand:
            print("あいこです")
        elif (user_hand == "グー" and computer_hand == "チョキ") or (user_hand == "チョキ" and computer_hand == "パー") or (user_hand == "パー" and computer_hand == "グー"):
            print("勝ちです")
        else:
            print("負けです")
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
            break
        # 入力がyでもnでもない場合はもう一度入力してもらう
        else:
            print("yかnを入力してください")
            continue
    print("じゃんけんゲームを終了します")

# main関数を実行
if __name__ == "__main__":
    main()
