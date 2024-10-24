# 萬年曆

month_name = ["January", "February", "March", "April", "May", "June", \
			"July", "August", "September","October", "November", "December"] # \ 是python將單一敘述分成多行的符號 後面不可加上任何字元
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 以串列儲存各月份的天數

year = int(input("請問你要列印西元哪一年的年曆："))
is_leap_year = (year % 400==0) or ((year % 4==0) and (year % 100!=0)) # 判斷是否為閏年（將布林運算式指定給變數is_leap_year，所以is_leap_year的值會是布林值）

if is_leap_year: # 若為閏年
	month_day[1] = 29 # 則 儲存各月份的天數的串列中索引值為1的元素的值 指定為 29（2月的天數由28變成29）

next_position = ((year-1) + (year-1)//4 - (year-1)//100 + (year-1)//400 + 1) % 7
# 4的倍數是閏年 但100的倍數不是閏年 400的倍數又是閏年

for j in range (1, 13) : # 外迴圈 從1到12（月）
	print(month_name[j-1]) # 依序印出month_name串列中的元素
	print ("SUN MON TUE WED THR FRI SAT")
	if next_position != 0:
		print("    "*next_position, end="") # 讓日期位置可以接著上個月份最後一天的位置繼續往右移
	for i in range (1, month_day[j-1]+1): # 內迴圈 從1到該月最後一天
		print(f"{i:3d}", end=" ")
		next_position += 1 # 將next_position原本的值+1在指定回給next_position
		if next_position == 7: 
			next_position = 0
			print() # 滿一週就換行（輸出資料 的 結尾符號 預設為 換行符號）
	print()