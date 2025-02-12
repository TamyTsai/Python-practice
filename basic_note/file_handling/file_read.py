# file.read()

# 一次讀取 整個檔案內容 為 一個字串
# 適合小型檔案，需要 處理 整個檔案內容時 使用

with open("scores.txt", "r", encoding="utf-8") as file: # 對「sample.txt」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
	content = file.read() # 將讀取到的檔案內容存入content變數
	lines = content.splitlines() # 將檔案內容根據換行做斷行處理，每一行變成一個元素，存入串ㄌㄧㄝ
	# 一次讀取一整個檔案，先將內容斷行處理
	# 檔案很大時，一次讀完會很耗時間

	for line in lines: # 對串列中的每一個元素進行以下處理
		name, score = line.strip().split(": ") # strip()：去掉最前面與最後面的空白符號 # split()：用什麼符號隔開
		scores = list(map(int, score.split(", "))) # split()：用什麼符號隔開 # map()：轉換資料型態
		# 將每個分數間用逗號隔開，資料型態轉成整數，再轉換為新串列
		average = sum(scores) / len(scores) # 將scores串列中的所有值加總，除以scores串列中的元素個數
		print(f"{name} 的總分是：{sum(scores)}, 平均分數是：{average:.2f}")