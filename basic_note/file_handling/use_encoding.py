# 使用encoding參數

file = open("sample.txt", "w") # 文字檔的預設編碼為UTF-8，開啟檔案的編碼方式不正確將會導致錯誤
# 對「sample.txt」檔案 使用「寫入檔案」（創建新檔或覆蓋舊檔）模式
# 並將檔案放入file變數
file.write("這是我的第一份文件\n") # 將字串"這是我的第一份文件\n"寫入檔案
file.write("這是第二行資料\n")
file.close() # 關閉檔案

file = open("sample.txt", "r") # 對「sample.txt」檔案 使用「讀取檔案」模式 
file_content = file.read() # 讀取檔案，並將讀取到的內容，存入file_content變數
print(f"檔案的內容為：\n{file_content}")
file.close()

with open("sample.txt", "r", encoding="big5") as file: # 因為檔案編碼方式是UTF-8，所以這裡會出錯
# 對「sample.txt」檔案 使用「讀取檔案」模式，編碼方式採BIG5，並將檔案放入file變數
	file_content = file.read()
	print(f"檔案的內容為：\n{file_content}")