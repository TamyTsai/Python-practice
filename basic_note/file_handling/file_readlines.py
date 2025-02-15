# file.readlines()

# 一次讀取所有資料，傳回一個 串列，其中 每個元素 是 文件中的一行（包含 換行符號）
# 適合需要 將 所有資料行 作為 列表 進行批次處理，或 需要 隨時 存取某一行 的應用情境

with open("scores.txt", "r", encoding="utf-8") as file: # 對「sample.txt」檔案 使用「讀取檔案」模式，編碼方式採UTF8，並將檔案放入file變數
	lines = file.readlines() # 一次讀取整個檔案，將每一行變成一個元素
for i in range(len(lines)):
		name, score = lines[i].strip().split(": ")
		scores = list(map(int, score.split(", ")))
		average = sum(scores) / len(scores)
		print(f"{name} 的總分是：{sum(scores)}, 平均分數是：{average:.2f}")

# 一次讀取整個檔案會比較花時間及耗費資源
# 串列有index，要讀取指定行數很方便