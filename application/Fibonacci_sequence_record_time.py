# 遞迴函式-費式數列最佳化

# 計算執行多次遞迴函式所需之時間

# 遞迴會使用大量記憶體，要小心避免導致系統當機
# 遞迴有時會導致重複計算，影響效率

from datetime import datetime # 引入datetime模組

def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

start_time = datetime.now()

num = 35
for i in range(0, num):
	print(fibonacci(i), end="")
	if i+1 != num:
		print(", ", end="")

end_time = datetime.now()
elapsed_time = end_time - start_time # 計算執行時間

print(f"\n執行時間：{elapsed_time}") # \n 為換行符號