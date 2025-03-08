# 函式的變數範圍-全域和區域變數

x = "Global" # 全域變數

def my_function():
	x = "Local" # 區域變數
	print(f'我在函式內部：{x}') # 在函式內部，優先取用區域變數。

my_function() # 呼叫函式。輸出「我在函式內部：Local」
print(f'我在函式外部：{x}') # 在函式外部，區域變數作用域不及此，故取用全域變數。輸出「我在函式外部：Global」

# ---

x = "Global" # 全域變數

def my_function():
	y = "Local" # 區域變數
	print(f'我在函式內部：{x}') # 在函式內部中找不到區域變數x，所以往外找，找到全域變數x

my_function() # 呼叫函式。輸出「我在函式內部：Global」
print(f'我在函式外部：{y}') # 在函式外部，區域變數作用域不及此，存取不到區域變數y。


# 函式的變數範圍-global關鍵字
x = "Global" # 全域變數

def my_function():
	global x # 於函式內部使用global關鍵字以存取全域變數
	# 在函式中使用外部的變數，建議使用global關鍵字以避免錯誤。養成良好的程式碼撰寫習慣，可增加程式碼可維護性
	x = "Modified Global"

print(f'執行函數前的x：{x}') # 輸出「執行函數前的x：Global」
my_function() # 呼叫函式。函式中存取全域變數x，並將其重新賦值為"Modified Global"
print(f'執行函數後的x：{x}') # 輸出「執行函數前的x：Modified Global」

# 函式的變數範圍-nonlocal關鍵字
x = "Global" # 全域變數

def outer_function():
	x = "Outer" # 外層函式的區域變數
	print(x) # 輸出指定給外層函式的區域變數的值。輸出"Outer"
	def inner_function():
		nonlocal x # 於 內層函式內部 使用nonlocal關鍵字，以存取 外層函式的區域變數
		x = "Modified Outer" # 將 外層函式的區域變數 重新賦值
		
	inner_function() # 呼叫內層函式（將外層函式的區域變數重新賦值）
	print(x) # 輸出"Modified Outer"

print(x) # 輸出「Global」
outer_function()
# 輸出「Outer」及「Modified Outer」