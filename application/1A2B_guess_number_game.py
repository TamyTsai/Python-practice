# 1A2B猜數字遊戲
secret_num="87"
guess=None
guess_count=0
guess_limit=6
out_of_limit=False
while secret_num!=guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess=input("請輸入你猜的數字(11~99之間)： ")
        if guess[0] == secret_num[1] and guess[1] == secret_num[0]:
            print("0A2B")
        elif guess[0] != secret_num[0] and guess[1] == secret_num[0] or guess[0] == secret_num[1] and guess[1] != secret_num[1]:
            print("0A1B")
        elif guess[0] != secret_num[0] and guess[1] != secret_num[1]:
            print("0A0B")
        elif guess[0] == secret_num[0] and guess[1] != secret_num[1] or guess[0] != secret_num[0] and guess[1] == secret_num[1]:
            print("1A0B")
    else:
        out_of_limit = True
if out_of_limit:
    print("猜超過6次，失敗了")
else:
    print("恭喜猜對")
# -->
# 請輸入你猜的數字(11~99之間)： 78
# 0A2B
# 請輸入你猜的數字(11~99之間)： 72
# 0A1B
# 請輸入你猜的數字(11~99之間)： 53
# 0A0B
# 請輸入你猜的數字(11~99之間)： 85
# 1A0B
# 請輸入你猜的數字(11~99之間)： 87
# 恭喜猜對