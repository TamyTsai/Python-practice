# 標準函式庫—數學與隨機亂數

import random # 引入Python標準函式庫含有的random模組
items = ["apple", "banana", "cherry", "date"] # 創建陣列
for i in range(3): # 用for迴圈執行固定次數之迴圈
	print(f"第{i+1}次抽籤結果：")
	print(f"隨機選一個：{random.choice(items)}") # 呼叫random模組中的choice函式
	print(f"第{i+1}次抽籤結果：{random.sample(items, 2)}") # 呼叫random模組中的sample函式
	# 隨機抽樣
	print() # 輸出函式之end參數預設為換行符號
	# print也是一個內建函式，不需import模組即可使用