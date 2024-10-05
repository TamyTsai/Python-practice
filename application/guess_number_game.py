# 猜數字遊戲
secret_num=77
guess=None #一定要先定義變數guess，要不然程式 會不知道 你下面的不等於 是在 不等於什麼
while secret_num!=guess:
    guess=int(input("請輸入你猜的數字： "))
    if guess > secret_num:
        print("再小一點")
    elif guess < secret_num:
        print("再大一點")
print("恭喜猜對") #當secret_num沒有!=guess時，就不會執行迴圈，直接執行這一條
# -->
# 請輸入你猜的數字： 50
# 再大一點
# 請輸入你猜的數字： 80
# 再小一點
# 請輸入你猜的數字： 77
# 恭喜猜對