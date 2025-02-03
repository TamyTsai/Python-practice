# 遞迴函式-河內塔

def hanoi(n, source, target, auxiliary, steps): # 定義河內塔遞迴函式

# 解決河內塔問題並顯示步驟
# :param n: 圓盤數量
# :param source: 起始柱子
# :param target: 目標柱子
# :param auxiliary: 輔助柱子
# :param steps: 步驟計算器
# :return: 更新的步驟計數

	if n == 1:
		# 基本條件：當只有一個圓盤時，直接搬移
		print (f"第 {steps[0] + 1}步：將圓盤從 {source} 搬到 {target}")
		steps[0] += 1
	else:
		# 先將 n-1 個圓盤從 source 搬到 auxiliary
		steps = hanoi(n - 1, source, auxiliary, target, steps)
		# 將第 n 個圓盤從 source 搬到 target
		print(f"第 {steps[0] + 1} 步：將圓盤從 {source}搬到 {target}")
		steps[0] += 1 # 將串列steps中第一個元素的值+1 後 重新指定給 串列steps中第一個元素
		# 最後將 n-1 個圓盤從 auxiliary 搬到 target
		steps = hanoi(n - 1, auxiliary, target, source, steps)
	return steps

def main(): # 定義主程式函式，在其中內嵌河內塔遞迴函式
	# 提示輸入圓盤數量
	num_disks = int(input("請輸入圓盤的數量："))
	print(f"開始解決河內塔問題，總共 {num_disks} 個圓盤。")

	# 初始化步驟計數
	steps = [0] # 使用列表以便在遞迴中更新
	hanoi(num_disks, 'A', 'C', 'B', steps)

	# 最終輸出總步驟
	print(f"\n完成！總共搬移了{steps[0]}步。")

if __name__ == "__main__":
	main()

# n = 3 時 hanoi函式執行：
# steps = hanoi(2 , source, auxiliary, target, steps) # 回傳[2]給變數steps（串列）
# print（f"第 {steps[0] + 1} 步：將圓盤從 {source}搬到 {target}") # 輸出「第3步：將圓盤從A搬到C」
# steps[0] += 1 # steps[0]變3
# steps = hanoi(2, auxiliary, target, source, steps) # 回傳[3]給變數steps（串列）
# return steps # 回傳steps（串列）

# n = 2 時 hanoi函式執行：
# steps = hanoi(1 , source, auxiliary, target, steps) # 回傳[1]給變數steps（串列）
# print（f"第 {steps[0] + 1} 步：將圓盤從 {source}搬到 {target}") # 輸出「第2步：將圓盤從A搬到C」
# steps[0] += 1 # steps[0]變2
# steps = hanoi(1, auxiliary, target, source, steps) # 回傳[2]給變數steps（串列）
# return steps # 回傳steps（串列）

# n = 1 時 hanoi函式執行：
# print (f"第 {steps[0] + 1}步：將圓盤從 {source} 搬到 {target}") # 輸出「第1步：將圓盤從A搬到C」
# steps[0] += 1 # steps[0]變1
# return steps # 回傳steps（串列）