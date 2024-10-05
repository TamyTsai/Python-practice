#建立一個基本計算機
#功能：讀取數字相加，顯示結果
#得到用戶輸入
name = input("請輸入你的名字： ")
age = input("請輸入你的年紀： ")
print("哈囉" + name + "你今年" + age + "歲")

#input函式會預設括弧內為 字串
number1 = input("請輸入第一個數字： ")
number2 = input("請輸入第二個數字： ")
print(number1 + number2)
# -->85

#所以用input()得到 用戶輸入的內容，讓變數替換為 該內容 後，還要將其轉換回 數字 --整數相加
number1 = input("請輸入第一個數字： ")
number2 = input("請輸入第二個數字： ")
print(int(number1) + int(number2))
# -->13

#--允許小數相加
number1 = input("請輸入第一個數字： ")
number2 = input("請輸入第二個數字： ")
print(float(number1) + float(number2))
# -->13.5