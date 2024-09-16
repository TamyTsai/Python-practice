# 基本資料型態&變數

# 字串
'你好'
# 包容字串之引號單雙皆可
# swift中，資料類型首字母要大寫，python中，只有布林值的是否首字母要大寫

# 數字
70
-87
160.5
160.555

# 布林值
True
False

# 變數

name = "小明"
age = 18
is_male = True
# 1.變數的名稱 只能是 英文、數字、_
# 2.變數的開頭 不可以是數字

# 字串安插 string interpolation
print("有一個人叫" + name)
print(name + "今年18歲")

name = "小綠"
print(name)
name = "小藍"
print(name)
name = 50
print(name)
name = True
print(name)
# 一個變數被修改（更新）後，後面的更動 不會 影響 前面的更動
# swift中的變數 變數名稱 宣告時前面要加 var，python則是直接打變數名稱