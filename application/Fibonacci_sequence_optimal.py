# 遞迴函式-費式數列最佳化

# 進行最佳化

from datetime import datetime # 引入datetime模組
from functools import lru_cache # lru_cache為一種 記憶化函數 快取機制
# LRU為Least Recently Used
# 快取替換策略
# 當快取超出設定的大小時，會移除最久未被使用的快取項

@lru_cache(maxsize=None)

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