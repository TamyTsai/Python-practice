# 檔案的讀取、寫入

#open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex:C:/User/......123.txt（斜線要 跟從 檔案總管複製的 相反）
# 相對路徑 以程式的位置做延伸 ex: 123.txt(表示前面已經有程式所在之絕對路徑)（要開的檔案 與 程式所在路徑 相同時 可用）

# mod3="r" 讀取
# mod3="w" 覆寫
# mod3="a" 在原先的資料後寫東西

file = open("123.txt",mode="r")
print(file.read())
file.close()
#關掉檔案才不會佔用電腦資源

#只讀部分資料
file = open("123.txt",mode="r")
print(file.readline()) #讀一行（寫兩次就是讀兩行）
print(file.readline()) #讀兩行
file.close()

#讀每一行
file = open("123.txt",mode="r")
for line in file:
    print(line) 
file.close()

#把每一行資料放到 列表 中
file = open("123.txt",mode="r")
print(file.readsline()) 
file.close()

#覆寫
file = open("123.txt",mode="w")
file.write("hello") 
file.close()

#新增
file = open("123.txt",mode="a", encoding="utf-8") #編碼方式utf-8才有支援中文
file.write("\n你好") 
file.close()

#寫完直接關檔案
with open("123.txt",mode="a", encoding="utf8") as file:
    file.write("\n你好")
