print("複利計算器")
principal = int(input("請輸入你的本金：")) # 將使用者輸入的本金，轉成整數資料型態，存入principal變數
annual_interest_rate = float(input("請輸年利率：")) # 將使用者輸入的年利率，轉成浮點數資料型態，存入annual_interest_rate變數
year = int(input("請輸入要存款多少年？")) # 將使用者輸入的存款期間，轉成整數資料型態，存入year變數
total_balance = principal # 將 本金 指定為 初始本利和（初始本利和 為 本金（尚未開始生利息））
print("\n計算的結果如下：")
for i in range(1, year+1): # for迴圈會將「範圍」內的「元素」都跑一遍，所以i會從1到year年被逐一於以下程式碼執行 
	print(f"第{i}年的本金為：{total_balance:5.2f}", end=", ")
	current_year_interest = total_balance * annual_interest_rate # 將 本金*年利率的值 指定為 當年的利息
	print(f"利息為：{current_year_interest:5.2f}", end=", ")
	total_balance += current_year_interest # 將 原本的本利和 加上 當年的利息 之值，指定成 新的本利和(至當年年底的本利和)
	print(f"到年底的本利和為{total_balance:5.2f}")