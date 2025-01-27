# 自訂異常處理—電子商務訂單項目檢查
# 當訂單項目數量為0時 觸發的異常

class EmptyOrderError(Exception): # 定義一個名為 EmptyOrderError 的例外類別，繼承自 Python 的內建 Exception 類別
# 用於表示當訂單的商品數量為零時，會引發的錯誤
	def __init__(self, order_id): # 定義 __init__ 方法，用於初始化 異常物件 的 屬性 接收參數 order_id，代表發生異常的訂單編號
		self.order_id = order_id # 將 order_id 儲存到物件的屬性中，以便後續存取
		super().__init__(f"訂單{order_id}無任何商品，無法處理！") # 呼叫父類別 Exception 的初始化方法，並傳入自訂的錯誤訊息

def process_order(order_id, items): # 定義一個函式 process_order，用來處理訂單
# order_id: 訂單編號
# items: 訂單中包含的商品列表
	# 處理訂單 # 檢查商品列表是否為空
	if not items or len(items) == 0: # if 條件成立時，表示訂單中沒有任何商品
	# not items: 若列表為空或 None，會返回 True
	# len(items) == 0: 檢查列表的長度是否為 0
		raise EmptyOrderError(order_id) # 引發自訂異常
		# 如果條件成立，表示訂單中無商品，則使用 raise 主動引發 EmptyOrderError
	
	# 如果訂單中有商品（即未觸發例外），這些語句將執行
	print(f"訂單{order_id}包含商品：{items}")  # 印出訂單的商品內容
	print("訂單處理成功！")

# 測試程式
try:
	process_order(123, []) # 測試 無商品的訂單
	# 呼叫 process_order 函式，測試一個無商品的訂單（訂單號為 123，商品列表為空 []）
	# 因為列表為空，函式內會引發 EmptyOrderError
except EmptyOrderError as e: # 捕捉 EmptyOrderError 異常，並將其對應的物件存入變數 e。
	print(f"捕捉到異常：{e}") # 異常的錯誤訊息（由 EmptyOrderError 提供）
	print(f"錯誤的訂單編號：{e.order_id}") # 發生錯誤的訂單編號（存儲在 e.order_id 中）