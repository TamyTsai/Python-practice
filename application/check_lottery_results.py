# 大樂透對獎程式

def check_lottery_results(lottery_file, winning_numbers, special_number):
	with open(lottery_file, "r", encoding="utf-8") as file: # 使用open開啟檔案
	# 對「lottery_file」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
		print("開獎結果：")
		print(f"開獎號碼：{sorted(winning_numbers)}，特別號：{special_number}\n")
		for line in file: # 讀取每組號碼（一組號碼一行）
		# 對 檔案物件 進行迭代，自動 逐行讀取，相當便利
		# 建議優先使用的 逐行讀取方式，特別適合 處理 大檔案 的 逐行讀取與處理
		# for line in file：直接做迴圈，相比readline的迴圈要自己寫 來得方便
			# 分割組別與號碼
			group, numbers = line.strip().split("：") # 利用冒號區隔出組別與號碼
			# 去掉號碼的中括號 並轉換為 整數集合
			player_numbers = set(map(int, numbers.strip("[]").split(", ")))
			# strip(”[]”)：拔掉中括弧
			# 用逗號分割六個數字，再將數字 轉為 整數的集合
			# 計算對中的號碼數
			# Python3 集合（set）是一個無序的不重複元素序列。 集合中的元素不會重重複，並且可以進行交集、並集、差集等常見的集合操作
			matched_numbers = winning_numbers & player_numbers # 將 winning_numbers集合 與 player_numbers集合 中 重複的元素，提取出來，放到 matched_numbers集合
			# 利用集合比對對中的號碼數（交集比對&）
			match_count = len(matched_numbers)
			is_special_matched = special_number in player_numbers
			# 是否包含（in）
			
			# 判斷中獎結果
			if match_count == 6:
				result = "頭獎"
			elif match_count == 5 and is_special_matched:
				result = "貳獎"
			elif match_count == 5:
				result = "參獎"
			elif match_count == 4 and is_special_matched:
				result = "肆獎"
			elif match_count == 4:
				result = "伍獎"
			elif match_count == 3 and is_special_matched:
				result = "陸獎"
			elif match_count == 3:
				result = "普獎 400元"
			elif match_count == 2 and is_special_matched:
				result = "柒獎"
			else:
				result = "未中獎"
			# 輸出結果
			print(f"{group}：對中{match_count}個號碼{'（含特別號）' if is_special_matched else ''}，中獎結果：{result}")
			
# 設定參數
lottery_file = "lottery_numbers.txt" # 之前產生的樂透號碼檔案
winning_numbers = {11, 40, 42, 45, 47, 49} # 本期開獎號碼（不含特別號）
# 集合
special_number = 27 # 本期特別號

# 執行對獎
check_lottery_results(lottery_file, winning_numbers, special_number)