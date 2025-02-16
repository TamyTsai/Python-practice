# 得知檔案大小：file.seek()及file.tell()

import os

file_path = "scores.txt"
file_size = os.path.getsize(file_path)
# 透過os模組得知檔案大小
print(f"檔案大小為：{file_size} 位元組")

with open(file_path, "r", encoding="utf-8") as file:
	file.seek(0, 2) # 將指標移動到檔案尾端
	# 移動 檔案 讀取指標 的 位置
	# file.seek(offset, whence)
	# offest：從 參考位置 要移動的 偏移量
	# whence：參考位置，預設為檔案的開頭
		# 0：檔案的開頭SEEK_SET
		# 1：檔案指標 目前的位置SEEK_CUR
		# 2：檔案的結尾SEEK_END
		# 比較建議用SEEK＿SET、SEEK＿CUR及SEEK＿END這三個系統的標準參數，可讀性比0 1 2 好
	print(f"檔案大小為：{file.tell()}位元組")
	# 回傳 目前 檔案指標 的位置（因為指標已經移動到檔案結尾，所以目前檔案的位置 可以代表 檔案大小）
	# 了解檔案目前 讀到 什麼地方 了
	# 以位元組為單位
	# 對於文字檔案來說，不等於字元數的位置，因為有的編碼方式 其字元 為 變動位元組（如：UTF-8）
	# 配合file.seek()來移動檔案的指標