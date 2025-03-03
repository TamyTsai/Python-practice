# 標準函式庫—文字處理與格式化

import re # 引入Python標準函式庫含有的re模組
# re：regular expression（正規表示式）

def validate_license_plate(plate):
	# 定義正則表達式
	pattern = r'[A-Z]{3}-\d{4}$'
	# 前綴r的作用是去除轉義字串
	# ^：開頭
	# [A-3]{3}：3個A-Z的字母
	# \d{4}：4個1-9的數字
	# $：結尾
	
	# 匹配輸入的車牌
	if re.fullmatch(pattern, plate): # 呼叫re模組中的fullmatch函式
	# match函式檢查字串中是否包含目標字串（從開頭開始，尋找第一個匹配的字元），fullmatch函式則是要求完全匹配
		return True
	else:
		return False

# 測試車牌
test_plates = [
	"ABC-1234", # 正確格式
	"AC-1234",
	"ABCDE-1234",
	"ABC-123",
	"abc-1234",
	"A1C-5678"
]

# 驗證車牌
for plate in test_plates: # 使用for迴圈來將範圍內的元素都跑一遍，執行固定次數的迴圈
	result = validate_license_plate(plate) # validate_license_plate(plate)函數會回傳True或False，將此值指定給result變數
	print(f"車牌{plate}的格式{'正確'if result else '錯誤'}") # 使用三元運算子來簡化敘述