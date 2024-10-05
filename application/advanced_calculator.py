# 建立一個計算機
num1=float(input("請輸入第一個數： "))
operator = input("請輸入運算符號： ")
num2=float(input("請輸入第二個數： "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("不支援的運算")

# -->
# 請輸入第一個數： 5    
# 請輸入運算符號： -
# 請輸入第二個數： 2.2
# 2.8

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： *
# 請輸入第二個數： 2.2
# 11.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： *
# 請輸入第二個數： 2.2
# 11.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： /
# 請輸入第二個數： 2.5
# 2.0

# -->
# 請輸入第一個數： 5
# 請輸入運算符號： ＃
# 請輸入第二個數： 2.2
# 不支援的運算