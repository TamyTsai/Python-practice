# 使用 for 迴圈來檢查 1 到 50 的數字
for num in range(1, 51):
    # 使用 if 條件判斷奇偶
    if num % 2 == 0:
        print(f"{num} 是偶數")
    else:
        print(f"{num} 是奇數")