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

# 列表list、列表的用法
#可以存放很多值的資料型態，當資料量多時，方便管理
score1 = 90
score2 = 70
score3 = 60
score4 = 50
score5 = 80
#化為列表（用「中括號」將資料們包起來）
scores = [90,70,60,50,80]
#(序數)      0  1  2  3  4
print(scores)
#存放字串
friends = ["小黑","小黃","小綠"]
print(friends)
#存放不同資料型態
things = [90,"小黑",True]
print(things)

#取得列表中之內容 print(列表名稱[序數])
print(scores[0])
#取得倒數第一位(序數用-1，不是-0，-0算0)
print(scores[-1])
#取得列表中一個範圍的資料 print(列表名稱[起始序數:最後序數（不含）])
print(scores[0:2])
print(scores[1:4])
#從 第幾個資料 取到 最後一個資料 print(列表名稱[起始序數:])
print(scores[1:])
#從 第一個資料 取到 第幾個個資料 print(列表名稱[:最後序數（不含）])
print(scores[:4])

phrase = "Hello Mr.White"
#         01234567
print(phrase[0:5])
print(phrase[6:])

#列表中資料替換 變數名稱[要被改之資料之序數] = 新值
scores[0] = 30
print(scores)

#列表函式
#延伸列表中資料 .extend()
scores.extend(friends)
print(scores)
#增加（從後面）列表中資料 .append()
scores.append(30)
print(scores)
#在列表中插入值 .insert(要插入的位置,要插入的值)
scores.insert(2,40)
print(scores)
#在列表中移除值 .remove() （有相同的值的話，只會移除列表中第一個）
scores.remove(30)
scores.remove("小黑")
print(scores)
#移除列表的最後一位 .pop() （括弧內不需要傳入值）
scores.pop()
print(scores)
#讓列表中資料以升冪排序 .sort() （括弧內不需要傳入值）
scores.remove("小黃")
scores.remove("小綠")
scores.sort()
print(scores)
#把列表做反轉 .reverse （括弧內不需要傳入值）
scores.reverse()
print(scores)
#顯示想要找的值在列表中的位置 .index(想要找的值)
print(scores.index(70))
#.index()會回傳第一個找到的值的位置
scores = [90,70,70,50,80]
print(scores.index(70))
#數列表中有幾個該資料 .count(想要數有幾個的資料)
print(scores.count(70))
print(scores.count(7))
#清除列表中所有資料，使其變成空列表 .clear() 括弧內不需要傳入值
scores.clear()
print(scores)
