# 標準函式庫—作業系統與檔案系統

# 列出當前目錄的所有檔案
import os # 引入Python標準函式庫含有的os模組
print(os.listdir('.'))  # 使用os模組中的listdir函式
# 列出當前目錄中的所有檔案和資料夾
# . 代表當前目錄
# .. 代表當前目錄的上一個目錄

# 建立暫存檔案
import tempfile  # 引入Python標準函式庫含有的tempfile模組
with tempfile.NamedTemporaryFile(delete=False) as temp_file: # 使用tempfile模組中的NamedTemporaryFile函式
# 此函式的操作與 TemporaryFile() 完全相同，但存在以下差異：
# 此函式回傳一個保證在檔案系統中具有可見名稱的檔案。
# 為了管理指定檔案，它使用 delete 和 delete_on_close 參數擴充 TemporaryFile() 來指定是否以及如何自動刪除指定檔案。
	temp_file.write(b"Hello, Temp File!") # 寫入暫存檔案
	# b前綴表示：後面字符串是bytes類型
	print(f"Temporary file created at: {temp_file.name}") # .name 是temp_file的一個属性，表示該臨時文件的完整路徑或名稱。
	# 暫存檔的檔名是自動給的