# 內建函式

# 內建函式-資料型別與轉換類
x = int("10") # 將字串10轉換為整數10
print(x)
y = list("abc") # 將字串abc轉換為列表['a', 'b', 'c']
print(y)

# 內建函式-數學運算類
print(abs(-5)) # 將-5取絕對值，輸出5
print(pow(2, 3)) # 2的3次方，輸出8

# 內建函式-序列與集合操作類
nums = [3, 1, 4]
print(sorted(nums)) # sorted() 函式可以排序可疊代物件(iterable) 並建立一個新的排序好的串列，故輸出： [1, 3, 4]
print(len(nums)) # len()函數可以用來回傳序列（如字符串、列表、元组）的長度，故輸出3

# 內建函式-輸出與輸入類
name = input("請輸入姓名：") # 接收使用者輸入
print(f"你好， {name}") # 輸出內容

# 內建函式-邏輯與條件判斷類
print(isinstance(5, int)) # isinstance() 函數可回傳一個對象是否是整數或浮點數。5是整數，故輸出True

value = [1, 2, 3]
if bool(value): # boo() 函數可回傳布林值。
# 在Python中，只有None、任何數值類型中的0、空字符串""、空元组()、空列表[]、空字典{}被視為False，其餘皆視為True。所以bool(value)會回傳True
	print("列表不是空的") # 因此會執行此區塊程式敘述
else:
	print("列表示空的")
	
# 內建函式-檔案與系統處理類
with open("example.txt", "w") as f: # open("檔案路徑", mode="開啟模式")
# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的資料後寫東西
	f.write("Hello, World!") # 在example.txt檔案中寫入Hello, World!