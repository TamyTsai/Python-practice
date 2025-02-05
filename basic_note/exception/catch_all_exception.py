# 捕捉所有異常

# 不確定可能會發生哪些錯誤
# 使用通用的Exception捕捉所有異常

try:
	print(10 / "A")
except Exception as e:
	print(f"捕捉到異常：{e}")
	
try:
	x = 10 / 0
except Exception as e:
	print(f"捕捉到異常：{e}")