# 如何使用數字、數字的用法
print(-77.2)
print(8+5)
print(8-5)
print(8*5)
print(8/5)
#整數除法(只顯示整數部分)
print(8//5)
#連續運算（有先乘除後加減）
print(8+8*5)
#括弧先算
print((8+8)*5)
#變數
number = 8
print(number*5)
#取餘數（％）
print(number%5)

#數字函式
#轉換資料型態為 字串（str()）
print(str(number))
#字串相連
print("會印出數字"+str(number))
#字串 與 數字 不能相加（字串間用加號 表示 字串的「串連」，數字間用加號 表示 數字的「相加運算」）（會出錯）
print(8+str(number))
#取絕對值 abs()
number = -8
print(abs(number))
#次方 pow(基數,次方)
print(pow(2,4))
#極大值 max()
print(max(2,3,88,100,78,11))
#極小值 min()
print(min(2,3,88,100,78,11))
#四捨五入 round()
print(round(4.4))
print(round(4.6))

#多一些數字函式可以用
from math import * 
#無條件捨去 floor() 地板
print(floor(4.6))
#無條件進位 ceil() 天花板
print(ceil(5.4))
#開根號 sqrt()
print(sqrt(64))