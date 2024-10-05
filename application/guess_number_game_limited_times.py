# 限制次數之猜數字遊戲
secret_num=77
guess=None
guess_count=0
guess_limit=3
out_of_limit=False
while secret_num!=guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess=int(input("請輸入你猜的數字： "))
        if guess > secret_num:
            print("再小一點")
        elif guess < secret_num:
            print("再大一點")
    else:
        out_of_limit = True
if out_of_limit:
    print("猜超過3次，失敗了")
else:
    print("恭喜猜對")
# -->
# 請輸入你猜的數字： 50
# 再大一點
# 請輸入你猜的數字： 80
# 再小一點
# 請輸入你猜的數字： 78
# 再小一點
# 猜超過3次，失敗了
# -----
# 請輸入你猜的數字： 50
# 再大一點
# 請輸入你猜的數字： 80
# 再小一點
# 請輸入你猜的數字： 77
# 恭喜猜對