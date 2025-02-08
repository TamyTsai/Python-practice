# 使用finally區塊

try:
	file = open("scores.txt", "r")
	print(file.read())
except FileNotFoundError:
	print("錯誤：檔案不存在！")
finally:
	# 無論如何都會執行的程式碼
	if file:
		file.close()