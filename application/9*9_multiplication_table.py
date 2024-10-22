# 巢狀迴圈

for i in range(1, 10): # 外迴圈 從1到9
	for j in range(2, 10): # 內迴圈 從2到9
		print(f"{j} x {i} = {j*i:2d}", end='\t') # :2d格式化整數輸出 佔兩個字元空間 設定結尾符號為跳位鍵
	print() # 換行