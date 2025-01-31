# 遞迴函式-費式數列

# 原始費式數列函式
def fibonacci(n):
	if n <= 1: # 基本條件：當n<=1時，直接回傳n
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

num = 6
for i in range(0, num): # 調整輸出格式
	print(fibonacci(i), end="") # 把輸出結尾預設的換行符號拿掉
	if i+1 != num: # 只要不要是最後一個數字
		print(", ", end="") # sep參數（輸出多項資料時的分隔符號）設為, end參數（輸出資料時的結尾符號）設為空字串

# 第1次迴圈：fibonacci(0)回傳0
# 第2次迴圈：fibonacci(1)回傳1
# 第3次迴圈：fibonacci(2)回傳fibonacci(1) + fibonacci(0) = 1 + 0 = 1
# 第4次迴圈：fibonacci(3)回傳fibonacci(2) + fibonacci(1) = fibonacci(1) + fibonacci(0) + 1 = 1 + 0 + 1 = 2
# 第5次迴圈：fibonacci(4)回傳fibonacci(3) + fibonacci(2) = fibonacci(2) + fibonacci(1) + 1 + 0 = fibonacci(1) + fibonacci(0) + 1 + 1 + 0 = 1 + 0 + 1 + 1 + 0 = 3
# 第6次迴圈：fibonacci(5)回傳fibonacci(4) + fibonacci(3) = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)  = fibonacci(2) + fibonacci(1) + 1 + 0 + fibonacci(1) + fibonacci(0) + 1  = fibonacci(1) + fibonacci(0) + 1 + 1 + 0 + 1 + 0 + 1 = 1 + 0 + 1 + 1 + 0 + 2 = 5

