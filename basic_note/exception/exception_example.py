# 常見的錯誤範例

# SyntaxError 語法錯誤
A = 1234
if a >= 0  # 沒加冒號
	print("A是正數")
else:
	print("A是負數")

# IndexError 超出範圍索引錯誤
A = [1, 2, 3]
print(A[3])
# A陣列索引值只到2

# TypeError 類型錯誤
A = "1234"
B = 1234
C = A + B # Python是強型別語言，將兩個不同型別的資料進行運算時，不允許型別轉換
print(C)

# ZeroDivisionError 除以零錯誤
A = 1234
B = 0
print(A/B)

# FileNotFoundError 檔案找不到錯誤
with open("scores.txt", "r", encoding="utf-8") as file:
	content = file.read()
	print(content)