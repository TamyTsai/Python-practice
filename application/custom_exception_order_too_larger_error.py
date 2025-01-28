# 自訂異常處理—電子商務訂單項目檢查 異常處理的擴展
# 當 訂單數量 超過限制時 引發的 異常

class OrderTooLargeError(Exception): # 定義了一個名為 OrderTooLargeError 的例外類別，繼承自 Python 的內建 Exception 類別
	def __init__(self, order_id, max_items): # 定義 __init__ 方法，用於初始化異常物件的屬性
	# order_id: 發生異常的訂單編號
	# max_items: 商品的最大允許數量
		self.order_id = order_id # 將訂單編號儲存到物件的屬性中，方便在異常處理時使用
		self.max_items = max_items # 將允許的最大商品數量儲存到物件屬性中
		super().__init__(f"訂單 {order_id} 的商品數量超過最大限制 {max_items}！")
		# 呼叫父類別 Exception 的初始化方法，並傳入自訂的錯誤訊息

def validate_order_size(order_id, items, max_items): # 定義了一個函式 validate_order_size，用來驗證訂單的商品數量是否超過限制
# order_id: 訂單編號
# items: 訂單中商品的列表
# max_items: 商品的最大允許數量
	if len(items) > max_items: # 如果 商品數量 超過 最大限制
		raise OrderTooLargeError(order_id, max_items) # 使用 raise 主動引發 OrderTooLargeError
		# 傳入 order_id 和 max_items，作為異常的附加資訊

# 測試程式
# 使用 try 區塊來測試函式 validate_order_size。
try:
	validate_order_size(123, ["item1", "item2", "item3"] * 5, 10)
	# 訂單編號：123
	# 商品列表：["item1", "item2", "item3"] * 5，這會產生 15 個商品的串列（因為串列重複了 5 次）
	# 最大允許數量：10
	# 因為商品數量（15）大於允許的最大數量（10），會引發 OrderTooLargeError
except OrderTooLargeError as e: # 使用 except 捕捉 OrderTooLargeError 異常
# 將 異常物件 存入 變數 e，以便後續處理
	print(f"捕捉到異常：{e}")
	print(f"錯誤的訂單編號：{e.order_id}")
	print(f"最大允許商品數：{e.max_items}")
	# 顯示發生異常的訂單編號和允許的最大商品數量