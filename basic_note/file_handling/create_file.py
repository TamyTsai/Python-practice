# 創建檔案

data = """ 李小明：80, 90, 100
王小華：95, 83, 77
張小英：100, 100 ,80
趙小安：79, 100 ,92
劉小雄：92, 88, 83
吳小美：96, 93, 100
"""

with open("scores.txt", "w", encoding="utf-8") as file: #  對「scores.txt」檔案 使用「寫入檔案」（創建新檔或覆蓋舊檔）模式，編碼方式採UTF-8，並將檔案放入file變數
	file.write(data) # 將 data變數中的值 寫入檔案