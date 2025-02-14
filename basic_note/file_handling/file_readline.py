# file.readline()

# 逐行讀取檔案，一次讀取一行，每次讀取後 指標 自動移動到下一行
# 適合需要 逐行處理檔案內容，但需要 精確 控制 每行的讀取

with open("scores.txt", "r", encoding="utf-8") as file: # 對「sample.txt」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
		while True: 
			line = file.readline() # 讀取檔案中的一行 
			if not line: # 如果讀取完檔案
				break # 就跳出迴圈
			name, score = line.strip().split(": ")
			scores = list(map(int, score.split(", ")))
			average = sum(scores) / len(scores)
			print(f"{name} 的總分是：{sum(scores)}, 平均分數是：{average:.2f}")