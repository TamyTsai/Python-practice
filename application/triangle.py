height = int(input("請輸入三角形的高度"))
for i in range(height):
	print((height-1-i)*" "+(1+2*i)*"*")
	
# 先把三角形用手畫出來
# 把每行 對應 多少* 多少空白 寫出來
# 找出i值 與 * 及 空白數量的關係公式