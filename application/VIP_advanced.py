# 優化寫法
is_vip = input("你是本戲院的 VIP 嗎？（y/n）").strip().upper()
# strip()可移除字串頭尾指定的字元（預設為空格或換行符），upper()可將答案轉為大寫
age = int(input("你的年紀是幾歲？"))

# 定義票價的字典
prices = {
    'Y': {True: 100, False: 60},   # VIP：年滿20為100元，未滿20為60元
    'N': {True: 200, False: 120}   # 非VIP：年滿20為200元，未滿20為120元
}

# 查詢對應票價
price = prices.get(is_vip, {'default': "無效的選項"}).get(age >= 20)
# .get(is_vip, {'default': "無效的選項"})：依據使用者的回答，從prices字典取出對應的value。如果使用者非輸入y或n，則回傳"無效的選項"
# .get(age >= 20, "無效的選項")：透過age >= 20所回傳的布林值，來決定要在第二層字典中取得哪一個value。

# 輸出結果
print(f"你{'是' if is_vip == 'Y' else '不是'}VIP, {'全票' if age >= 20 else '半票'}{price}元")
# 使用三元運算子(ternary conditional operator)以簡化程式碼
# 若is_vip == 'Y'，則顯示：你「是」VIP，否則顯示：你「不是」VIP
# 若if age >= 20，則顯示：「全票」，否則顯示：「半票」