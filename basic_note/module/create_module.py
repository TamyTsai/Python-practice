# 模組的創建

module_code = """
MY_PI = 3.14

def greet(name):
	return f'Hello, {name}!'

def circle_area(radius):
	return MY_PI*radius**2
"""
# 指定此串內容給變數module_code

# 將module_code變數中之內容，寫入到my_module.py檔案
with open('my_module.py', 'w') as f: # 將my_module.py檔案取別名為f
# open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex:C:/User/......123.txt（斜線要 跟從 檔案總管複製的 相反）
# 相對路徑 以程式的位置做延伸 ex: 123.txt(表示前面已經有程式所在之絕對路徑)（要開的檔案 與 程式所在路徑 相同時 可用）
# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的資料後寫東西
	f.write(module_code) # 在f檔案中，寫入module_code變數中之內容（現在該檔案中有一個變數和兩個函式了）

print("模組 my_module.py 已建立！")