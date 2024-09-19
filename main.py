# 基本資料型態&變數

# 字串
'你好'
# 包容字串之引號單雙皆可
# swift中，資料類型首字母要大寫，python中，只有布林值的是否首字母要大寫

# 數字
70
-87
160.5
160.555

# 布林值
True
False

# 變數

name = "小明"
age = 18
is_male = True
# 1.變數的名稱 只能是 英文、數字、_
# 2.變數的開頭 不可以是數字

# 字串安插 string interpolation
print("有一個人叫" + name)
print(name + "今年18歲")

name = "小綠"
print(name)
name = "小藍"
print(name)
name = 50
print(name)
name = True
print(name)
# 一個變數被修改（更新）後，後面的更動 不會 影響 前面的更動
# swift中的變數 變數名稱 宣告時前面要加 var，python則是直接打變數名稱

# 如何使用字串、字串的用法
# 換行
print("Hello \nMr.White")

# Hello" Mr.White
print("Hello\" Mr.White")
# \告訴程式說 引號 是字串的一部分

# 字串的相連
print("Hello" + "Mr.White")

# 變數
phrase = "Hello"
print(phrase + "Mr.white")

# 字串函式 function（資料運算處理，回傳資料）
# .lower() 變成小寫
# .upper() 變成大寫
# .islower() 檢查是否為小寫
# .isupper() 檢查是否為大寫
phrase = "Hello Mr.White"
print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.isupper())
# 函式疊加
print(phrase.lower().islower())

# Hello Mr.White
# 012345678
# 用位置找字母
print(phrase[1])
print(phrase[0])
print(phrase[6])
print(phrase[5])
# .index("") 找字的位置
print(phrase.index("H"))
print(phrase.index("M"))
print(phrase.index("l"))
# 若有好幾個一樣的字，會回傳第一個的位置

# .replace("被替代之字串","替代後之字串") 替代函式
print(phrase.replace("H","h"))
print(phrase.replace("l","L"))

# 如何使用數字、數字的用法
print(-77.2)
print(8+5)
print(8-5)
print(8*5)
print(8/5)
#整數除法(只顯示整數部分)
print(8//5)
#連續運算（有先乘除後加減）
print(8+8*5)
#括弧先算
print((8+8)*5)
#變數
number = 8
print(number*5)
#取餘數（％）
print(number%5)

#數字函式
#轉換資料型態為 字串（str()）
print(str(number))
#字串相連
print("會印出數字"+str(number))
#字串 與 數字 不能相加（字串間用加號 表示 字串的「串連」，數字間用加號 表示 數字的「相加運算」）（會出錯）
print(8+str(number))
#取絕對值 abs()
number = -8
print(abs(number))
#次方 pow(基數,次方)
print(pow(2,4))
#極大值 max()
print(max(2,3,88,100,78,11))
#極小值 min()
print(min(2,3,88,100,78,11))
#四捨五入 round()
print(round(4.4))
print(round(4.6))

#多一些數字函式可以用
from math import * 
#無條件捨去 floor() 地板
print(floor(4.6))
#無條件進位 ceil() 天花板
print(ceil(5.4))
#開根號 sqrt()
print(sqrt(64))

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

#所以用imput()得到 用戶輸入的內容，讓變數替換為 該內容 後，還要將其轉換回 數字 --整數相加
number1 = input("請輸入第一個數字： ")
number2 = input("請輸入第二個數字： ")
print(int(number1) + int(number2))
# -->13

#--允許小數相加
number1 = input("請輸入第一個數字： ")
number2 = input("請輸入第二個數字： ")
print(float(number1) + float(number2))
# -->13.5

