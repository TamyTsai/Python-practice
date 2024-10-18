# 多重選擇 的 條件判斷

sweetness_level = input("請選擇你要的甜度：（1）正常甜度, （2）半糖, （3）微糖, （其他）不加糖： ")  # 將使用者輸入答案字串，指定給sweetness_level變數
if sweetness_level== '1': # 條件為真時，執行以下敘述
	print("你選擇的是正常甜度，加4匙糖")
elif sweetness_level== '2': # 前一條件不為真，且本條件為真時，執行以下敘述
  print("你選擇的是半糖，加2匙糖")
elif sweetness_level== '3':
  print("你選擇的是微糖，加1匙糖")
else: # 前面所有條件皆不為真時，執行以下敘述
	print("你選擇的是不加糖")

# Ruby中的elif為elsif
# JavaScript中的elif為else if