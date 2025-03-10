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

# -------------------

# 定義函式（副程式：函數及程序）
# 定義函數
def 函數名稱(參數1, 參數2): # 有回傳值的副程式稱為「函數（function）」
	# 函數主體（必須內縮）
	return "回傳值"
# 定義程序
def greeting(): # 沒有回傳值的副程式則稱為「程序（procedure）」
	print("Hello!!!")
     
# 呼叫函式
greeting()

# 副程式在使用前必須先宣告
result = add(3, 5) # 不可未宣告就呼叫
# 大多數的程式語言，要求副程式在使用前必須先宣告，目的是檢查副程式的「呼叫」，與副程式的「宣告」是否一致，Python也不例外。
print(result)

def add(a, b):
	return a + b 

# 參數與引數數量要一致
def add(a, b): # 在呼叫函式時，提供給函式的資料稱為引數（argument），接受引數的稱為參數（parameter），故此處a及b為參數
	return a + b

result = add(3) # 此處3為引數，參數與引數數量不可不同
print(result)

# 注意函式是否有回傳值
def greeting(): # 程序
	print("Hello")
	
def add(a, b): # 函數
	return a+b

res = greeting() # 因為greeting為「程序」，屬於不會回傳值的副程式，故本行敘述作用僅僅為呼叫greeting程序，因此輸出Hello，並未將任何值指定給res變數
add(3, 5) # add為「函數」，屬於有回傳值的副程式，但該程序中之敘述未有輸出任何東西之敘述，且此處未將呼叫函數所得到的回傳值指定給任何變數，故本行敘述無作用
print(res) # 因前面沒有將任何值指定給res變數，故輸出的結果為「None」