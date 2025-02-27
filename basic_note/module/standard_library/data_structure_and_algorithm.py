# 標準函式庫—資料結構與演算法

from collections import Counter # 從 collections模組 引入 Counter類別
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)
# Counter 是在 Python 3.1 之後加入的新類別(class)
# python的命名風格：類別名稱使用大駝峰式命名法；模組名稱使用全小寫命名法（蛇式）
print(count)

import statistics # 引入statistics模組
data = [10, 20, 30, 40, 50]
print(f"平均值等於：{statistics.mean(data)}") # 呼叫statistics模組之mean函式，計算平均值
print(f"標準差為：{statistics.stdev(data)}") # 呼叫statistics模組之stdev函式，計算標準差