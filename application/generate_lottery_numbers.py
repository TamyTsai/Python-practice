# 大樂透電腦選號程式

import random # 使用random模組

def generate_lottery_numbers(num_sets, filename):
	with open(filename, "w", encoding="utf-8") as file: # 對「filename」檔案 使用「寫入檔案」（創建新檔或覆蓋舊檔）模式，編碼方式採UTF8，並將檔案放入file變數
	# 對「filename」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
		for i in range(1, num_sets + 1): # 跑num_sets次迴圈
			# 隨機選取6個不同的數字
			numbers = sorted(random.sample(range(1, 50), 6))
			# random.sample()可以設定數字範圍，一次產生多個數字
			# 產生6個1~49的數字
			# sorted()可以排序
			# 寫入檔案
			file.write(f"組{i}：{numbers} \n") # 將產生的結果數字寫入檔案
	print(f"已成功 {num_sets} 組號碼並寫入檔案'{filename}'")

# 設定參數
num_sets = 10 # 產生10組號碼
output_file = "lottery_numbers.txt" # 輸出檔案名稱

# 執行程式
generate_lottery_numbers(num_sets, output_file)