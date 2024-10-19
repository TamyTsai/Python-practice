# for 迴圈

sum = 0 # 指定數值0給變數sum
n = int(input("請輸入要從1累加到多少？")) # 將使用者輸入的字串數字轉換為整數資料型態後，指定給變數n
for i in range(1, n+1): # for迴圈會將「範圍」內的「元素」都跑一遍，所以i會從1到n被逐一於以下程式碼執行
	sum = sum + i
print(f"從 1 累加到{n}的結果是：{sum}")

# 範圍中第一個元素1進入sum = sum + i，sum由0變為1
# 範圍中第二個元素2進入sum = sum + i，sum由1變為3
# 範圍中第三個元素3進入sum = sum + i，sum由3變為6
# ....