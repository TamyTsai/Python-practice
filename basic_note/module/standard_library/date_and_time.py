# 標準函式庫—日期與時間

from datetime import datetime # 從Python標準函式庫含有的datetime模組 引入 datetime函式
now = datetime.now() # 將當前的時間存入now變數
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 將當前時間以指定格式顯示

from datetime import date # 從Python標準函式庫含有的datetime模組 引入 date函式
date1 = date(2024, 1, 1)
date2 = date(2024, 11, 17)
delta = date2 - date1 # 化成date格式 就可以做運算
print(f"日期差距為: {delta.days}") # .days：以天為單位