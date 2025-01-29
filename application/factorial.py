# 遞迴函式-計算階乘

def factorial(n):
	if n == 0: # 當問題簡化到某個程度時
		return 1 # 直接回傳結果
		# 用明確的結束條件（基本條件），確保遞迴不會無限執行
		# 基本條件：當n為0時，階乘為1（直接回傳結果）
	else: # 遞迴關係： n! = n * (n-1)!
		return n * factorial(n - 1) # 遞迴關係：問題被分解為更小的子問題，這些子問題被以相同的邏輯進行處理

print(factorial(5))
# factorial(5)回傳 5 * factorial(4)
# factorial(4)回傳 4 * factorial(3)
# factorial(3)回傳 3 * factorial(2)
# factorial(2)回傳 2 * factorial(1)
# factorial(1)回傳 1 * factorial(0)
# factorial(0)回傳 1（基本條件觸發，結束遞迴）
# 所以factorial(5)回傳 5 * 4 * 3 * 2 * 1 * 1 = 120