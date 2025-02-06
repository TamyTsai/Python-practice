# 使用else區塊

try:
	# 嘗試執行 的 程式碼
	num = int(input("請輸入一個整數："))
	print(f"你輸入的整數是：{num}")
except ValueError:
	# 異常處理
	print("錯誤：必須數入整數！")
else:
	# 如果未發生異常，執行這段程式碼（有條件地 執行）
	print("程式成功執行，未發生任何錯誤。")