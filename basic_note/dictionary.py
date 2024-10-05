# 字典dictionary
#   key        value
#    鍵          值
# 要查的單字   單字的解釋

dic = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dic)
print(dic["蘋果"])
print(dic["貓"])
# -->
# {'蘋果': 'apple', '香蕉': 'banana', '貓': 'cat', '狗': 'dog'}
# apple
# cat
# （*python的字典創建方法是 字典名稱={鍵:值}）
# (*swift的字典創建方法是 var/let 字典名稱=[鍵:值])

# 鍵跟值也 可以是 不同 資料類型
dic = {0:"apple",1:"banana",2:"cat",3:"dog"}
print(dic)
print(dic[0])
print(dic[1])
# -->
# {0: 'apple', 1: 'banana', 2: 'cat', 3: 'dog'}
# apple
# banana