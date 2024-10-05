# for 迴圈

#for 變數 in 字串or列表:
#    要重複執行的程式碼

for letter in "小白你好":
    print(letter)
# -->
# 小
# 白
# 你
# 好

# for num in [0,1,2,3,4]:
#     print(num)
# -->
# 0
# 1
# 2
# 3
# 4

#跑幾次迴圈 取決於 字串長度 或 列表資料數

#函式range
for num in range(10):
    print(num)
# -->
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# (不含最後一個數)

for num in range(2,7):
    print(num)
# -->
# 2
# 3
# 4
# 5
# 6

#寫出如同pow(2,5)函式效果的函式
#base_num2*2*2*2*2
def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result*base_num
    return result
print(power(2,5))
# -->
# 32