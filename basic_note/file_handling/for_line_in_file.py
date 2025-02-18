# for line in file:

# 對 檔案物件 進行迭代，自動 逐行讀取，相當便利
# 建議優先使用的 逐行讀取方式，特別適合 處理 大檔案 的 逐行 讀取與處理
# for line in file：直接做迴圈，相比readline的迴圈要自己寫 來得方便

with open("scores.txt", "r", encoding="utf-8") as file: # 對「scores.txt」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
	for line in file:
		name, score = line.strip().split(": ")
		scores = list(map(int, score.split(", ")))
		average = sum(scores) / len(scores)
		print(f"{name} 的總分是：{sum(scores)}, 平均分數是：{average:.2f}")