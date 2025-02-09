# 多個except區塊的使用

def bmi(weight, height):
	try:
		return int(weight) / (int(height)/100)**2
	except ZeroDivisionError:
		print("錯誤：不能除以零！")
		return None
	except ValueError: # 為不同類別的錯誤，客製化不同的 異常處理程式碼
		print("錯誤：請輸入數字！")
		return None
weight = input("請問你的體重？")
height = input("請問你的身高？")
if bmi_value := bmi(weight, height):
	print(f"你的BMI為：{bmi_value:.2f}")
