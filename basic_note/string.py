# 如何使用字串、字串的用法
# 換行
print("Hello \nMr.White")

# Hello" Mr.White
print("Hello\" Mr.White")
# \告訴程式說 引號 是字串的一部分

# 字串的相連
print("Hello" + "Mr.White")

# 變數
phrase = "Hello"
print(phrase + "Mr.white")

# 字串函式 function（資料運算處理，回傳資料）
# .lower() 變成小寫
# .upper() 變成大寫
# .islower() 檢查是否為小寫
# .isupper() 檢查是否為大寫
phrase = "Hello Mr.White"
print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.isupper())
# 函式疊加
print(phrase.lower().islower())

# Hello Mr.White
# 012345678
# 用位置找字母
print(phrase[1])
print(phrase[0])
print(phrase[6])
print(phrase[5])
# .index("") 找字的位置
print(phrase.index("H"))
print(phrase.index("M"))
print(phrase.index("l"))
# 若有好幾個一樣的字，會回傳第一個的位置

# .replace("被替代之字串","替代後之字串") 替代函式
print(phrase.replace("H","h"))
print(phrase.replace("l","L"))