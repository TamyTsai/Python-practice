# 元組 tuple
#建立元組
#取得元組中之資料（用小括號將資料包起來）
scores = (90,80,60,70,50)
#顯示元組中特定位置之值 （中括號[序數]）
print(scores[0])
print(scores[0:2])
#取得元組之長度（資料筆數） len(元組名稱) (也可以用在列表)
print(len(scores))

#元組與列表之差異--元組一旦創建，不能做新增、修改或刪除--防止資料被意外修改
scores[0] = 30
print(scores)
# (TypeError: 'tuple' object does not support item assignment)