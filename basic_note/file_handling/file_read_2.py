# file.read(1)

with open("scores.txt", "r", encoding="utf-8") as file: # 對「sample.txt」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
	while True: # 除非遇到break，否則不會跳出迴圈
		char = file.read(1) # 一次讀取檔案內容的一個字元，並放入char變數
		# 跑的速度會比read()慢
		# 不同編碼方式 一個字元 所佔用的 位元組 數量 不同，但read()函式可以自行判斷
		if not char: # 如果是空字串（檔案的內容已經被讀完）
			break # 跳出迴圈
		elif char == "\n": # 如果遇到換行符號
			name, score = line.strip().split(": ")
			scores = list(map(int, score.split(", ")))
			average = sum(scores) / len(scores)
			print(f"{name} 的總分是：{sum(scores)}, 平均分數是：{average:.2f}")
			line = ""
		else:
			line = line + char # 將字元加在原本的句子後面