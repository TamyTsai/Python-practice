# 使用with開啟檔案

with open("sample.txt", "r") as file: 
# 對「sample.txt」檔案 使用「讀取檔案」模式，並將檔案放入file變數
# 使用with語法，在檔案操作完成後會自動關閉
# 離開with範圍，檔案就關閉了
	file_content = file.read() # 讀取檔案，並將讀取到的內容，存入file_content變數
	print(f"檔案的內容為：\n{file_content}")