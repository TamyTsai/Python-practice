# 優化寫法
sweetness_level = input("請選擇你要的甜度：(1)正常甜度, (2)半糖, (3)微糖,（其他）不加糖：")

sugar_amount = {
    '1': "正常甜度, 加4匙糖",
    '2': "半糖, 加2匙糖",
    '3': "微糖, 加1匙糖"
} # 用字典存放選項及答案

print(f"你選擇的是{sugar_amount.get(sweetness_level, '不加糖')}")
# 使用get()方法可以透過key來獲取字典中對應的value，如果key不存在，則回傳'不加糖'（get()的第二個參數作為key不存在時的預設值）