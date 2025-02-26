# 寫入與讀取檔案資料

file = open("sample.txt", "w") # 對「sample.txt」檔案 使用「寫入檔案」（創建新檔或覆蓋舊檔）模式
# 並將檔案放入file變數
file.write("這是我的第一份文件\n") # 將字串"這是我的第一份文件\n"寫入檔案
file.write("這是第二行資料\n")
file.close() # 關閉檔案
# 關閉檔案後才會釋放資源，並將未寫入的資料，確實寫入檔案中
# 檔案未關閉前，資料可能只存在緩衝區（buffer）而已

file = open("sample.txt", "r") # 對「sample.txt」檔案 使用「讀取檔案」模式 
file_content = file.read() # 讀取檔案，並將讀取到的內容，存入file_content變數
print(f"檔案的內容為：\n{file_content}")
file.close() # 關閉檔案