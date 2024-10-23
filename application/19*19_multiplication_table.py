# 巢狀迴圈

for i in range(1, 20): # 外迴圈 從1到19
	for j in range(2, 20): # 內迴圈 從2到19
		print(f"{j} x {i:2d} = {j*i:3d}", end='\t') # :2d格式化整數輸出 佔兩個字元空間 設定結尾符號為跳位鍵
	print() # 換行