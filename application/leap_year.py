year = int(input("請輸入西元年： "))  # 將使用者輸入的西元年字串轉為整數後，指定給year變數
is_leap_year = (year % 400==0) or ((year % 4 ==0) and (year % 100 !=0))
# 可以被400整除 或是 可以被4整除但不能被100整除 的年份 是閏年
# or邏輯運算子 在其一條件為真時，即為真
# and邏輯運算子 僅在所有條件為真實，方為真
if is_leap_year:
	print(f"西元{year}是閏年") # 若是閏年 就執行此段程式碼
else:
	print(f"西元{year}是平年") # 若非閏年 就執行此段程式碼
