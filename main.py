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

# 元組 tuple
#建立元組
#取得元組中之資料（用小括號將資料包起來）
scores = (90,80,60,70,50)
#顯示元組中特定位置之值 （中括號[序數]）
print(scores[0])
print(scores[0:2])
#取得元組之長度（資料筆數） len(元組名稱) (也可以用在列表)
print(len(scores))

#元組與列表之差異--元組一旦創建，不能做新增、修改或刪除--防止資料被意外修改
scores[0] = 30
print(scores)
# (TypeError: 'tuple' object does not support item assignment)

# 函式 function（一段預先寫好的程式碼，幫我們做運算，回傳資料）
# 定義函式 def函式名稱(參數名): 希望函式做的動作（寫在函式內部（在函式的下一行，前面空4個空白鍵，或一個Tab鍵））
# 函式命名規則 與 變數命名規則 相同
def hello():
    print("hello")
# 呼叫函式
hello()
# -->hello

# 能處理資料之函式
def hello(name,age):
    print("hello，" + name + "你今年" + age + "歲" )
hello("小白","24")
# -->hello，小白你今年24歲
#24要加引號，使其變成字串（使age的資料類型變成字串），要不然會因為24是數字，不能跟字串「你今年」「歲」做相加運算 的原因，而產生錯誤
#或是在函式內部中 將age變數就先做轉變成字串之處理
def hello(name,age):
    print("hello，" + name + "你今年" + str(age) + "歲" )
hello("小白",24)
# -->hello，小白你今年24歲

#練習：定義一個函式，函式名稱為add，函式功能為將傳入函式之兩個數字 作相加 並顯示出來
def add(num1,num2):
    print(num1+num2)
add(8,5.5)
# -->13.5
#**回傳return return的值 會覆蓋掉 呼叫的值
def add(num1,num2):
    print(num1+num2)
    return 10
print(add(8,5.5))
# -->13.5
#    10
#希望回傳 第一個值 與 第二個值 相加 的 結果 
def add(num1,num2):
    #print(num1+num2)
    return num1+num2
print(add(8,5.5))
# -->13.5
#程式看到 名為add函式的定義，然後 看到我們呼叫該函式，最後又看到該函式被返回到num1+num2的值，這個值就取代掉 add(8,5.5)

#為何用return而不用print，因為通常不是運算完就結束了，我們可能還要對被回傳的值做更多的運算和處理

#程式碼首先看到我們定義了名為add的函式
#然後看到我們呼叫add(8,5.5)，然後他會往上找到並運行函式內部的程式碼
#函式內部第一行運作「印出num1+num2」，所以先顯示13.5
#程式碼碰到return 10，所以value的值被覆蓋為10
#最後我們print value，所以又出現一個10
def add(num1,num2):
    print(num1+num2)
    return 10
value=add(8,5.5)
print(value)
# -->13.5
#    10
#函式運作中沒寫return，會出現什麼？
#如果函式運作碼中沒有return東西，python會預設為None（類似swift之Nil）（預設加入 return None），所以add(8,5.5)會變成None，value也因此變成None
def add(num1,num2):
    print(num1+num2)
    #return None
value=add(8,5.5)
print(value)
# -->13.5
#    None
#函式中的運作碼，碰到return就會直接結束（print("你好")顏色變淡，不會被執行）
def add(num1,num2):
    print(num1+num2)
    return None
    print("你好")
value=add(8,5.5)
print(value)
# -->13.5
#    None

# if判斷句

# 1.
# 如果 我肚子餓
#     我就去吃飯
hungry=True
if hungry:
    print("我就去吃飯")
# -->我就去吃飯
# (*在swift中，if後面不用加冒號，接的是大括弧)

hungry=False
if hungry:
    print("我就去吃飯")
# -->(會跳過if判斷句中的程式碼，但後面沒東西了，所以沒有程式碼被執行)


# 2.
# 如果今天下雨
#    我就開車去上班
# 否則
#    我就走路去上班
rainy=True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")
# -->我就開車去上班

rainy=False
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")
# -->我就走路去上班


# 3.
# 如果 你考100分
#    我給你1000元
# 或是如果 你考80分以上
#    我給你500元
# 或是如果 你考60分以上
#    我給你100元
# 否則
#    你給我300元
score=100
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")
# -->我給你1000元
# （*swift中的「或是如果」是else if）

score=90
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")
# -->我給你500元

score=50
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")
# -->你給我300元


# 4.
# 如果 你考100分 且 今天下雨
#     我給你1000元
# 否則
#     你給我100元
score=100
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->我給你1000元
# （*swift中的「且」是&&）

score=90
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->你給我100元

score=100
rainy=False
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->你給我100元


# 5.
# 如果 你考100分 或 今天下雨
#     我給你1000元
# 否則
#     你給我100元
score=100
rainy=True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->我給你1000元
# （*swift中的「或」是||）

score=90
rainy=True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->我給你1000元

score=90
rainy=False
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")
# -->你給我100元


# 6.
# 如果 你考100分 或 沒有下雨
#     我給你1000元
# 否則
#     你給我100元
score=100
rainy=True
if score==100 and not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")
# -->你給我100元
# （*swift中的「not」是!）

score=100
rainy=False
if score==100 and not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")
# -->我給你1000元


# 7.
# 如果 你沒有考100分 或 沒有下雨
#     我給你1000元
# 否則
#     你給我100元
score=100
rainy=True
if score!=100 and not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")
# -->你給我100元

score=90
rainy=False
if score!=100 and not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")
# -->我給你1000元

#回傳函式中最大的數
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(2,3,5))
# -->5

# 建立一個計算機
num1=float(input("請輸入第一個數： "))
operator = input("請輸入運算符號： ")
num2=float(input("請輸入第二個數： "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("不支援的運算")

# -->
# 請輸入第一個數： 5    
# 請輸入運算符號： -
# 請輸入第二個數： 2.2
# 2.8

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： *
# 請輸入第二個數： 2.2
# 11.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： *
# 請輸入第二個數： 2.2
# 11.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： /
# 請輸入第二個數： 2.5
# 2.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： ＃
# 請輸入第二個數： 2.2
# 不支援的運算

# 字典dictionary
#   key        value
#    鍵          值
# 要查的單字   單字的解釋

dic = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dic)
print(dic["蘋果"])
print(dic["貓"])
# -->
# {'蘋果': 'apple', '香蕉': 'banana', '貓': 'cat', '狗': 'dog'}
# apple
# cat
# （*python的字典創建方法是 字典名稱={鍵:值}）
# (*swift的字典創建方法是 var/let 字典名稱=[鍵:值])

# 鍵跟值也 可以是 不同 資料類型
dic = {0:"apple",1:"banana",2:"cat",3:"dog"}
print(dic)
print(dic[0])
print(dic[1])
# -->
# {0: 'apple', 1: 'banana', 2: 'cat', 3: 'dog'}
# apple
# banana

# while 迴圈（while迴圈與if陳述句類似，其檢查條件是否為真，並在條件保持正確狀態下，重複執行代碼塊）

i=1
while i<=5:
    print(i)
    i += 1
    #相當於 i=i+1 也就是i會一直增加1
print("迴圈結束")
# -->
# 1
# 2
# 3
# 4
# 5
# 迴圈結束

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
