# try-except基本語法

try:
	# 嘗試執行的程式碼
	print(10 / 0)
except ZeroDivisionError: # 錯誤的類別
	# 異常處理程式碼
	print("發現到異常：不能除以零")