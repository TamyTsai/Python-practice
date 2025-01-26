# 自訂異常處理—年齡輸入檢測

class InvalidAgeError(Exception): # 宣告類別
# InvalidAgeError類別 繼承自 Python 的內建 Exception 類別，Exception為其父類別
# 從現有的內建異常，再另外制訂客製化的異常
	"""當年齡無效時 引發的異常"""
	def __init__(self, age): # 初始 化例外類別 的 實體 時，會執行這段程式碼
	# 參數age接收使用者提供的無效年齡，並將其儲存在 self.age 中
		self.age = age
		super().__init__(f"年齡 {age} 錯誤，必須大於等於0!")
		# 呼叫父類別 Exception 的初始化方法，並傳入一個錯誤訊息（上下文傳遞）

# 測試自訂異常處理
try:
	age = int(input("請輸入年齡："))
	if age < 0:
		raise InvalidAgeError(age) # 使用 raise 主動引發 InvalidAgeError 例外
		# 傳入用戶輸入的年齡值，讓例外物件包含相關資訊
except InvalidAgeError as e:
	print(e)
except ValueError:
	print("輸入的不是整數！")
except Exception: # 捕捉所有其他未特別處理的例外（通用例外類型）。
	print("發生未知錯誤")