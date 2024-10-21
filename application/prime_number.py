# 多重for迴圈

for num in (5,8,11,13,17,20): # 集合，無序不重複元素序列
    for i in range(2, num//2):
        if num % i == 0:
            print(num, '不是質數')
            break
    else:
        print(num, '是質數')

"""
num    i in range(2, num//2)    num % i ==0                                是否break
5      i in range(2, 2)         （range不包含結束值，所以這裡不會執行）          否，故進入else後敘述
8      i in range(2, 4)         8 % 2 ==0                                  是，內迴圈結束，不進入else後敘述，回到外迴圈
11     i in range(2, 5)         11 % 2 !=0
                                11 % 3 !=0
                                11 % 4 !=0                                 否，故進入else後敘述
"""