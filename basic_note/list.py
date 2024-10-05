# 列表list、列表的用法
#可以存放很多值的資料型態，當資料量多時，方便管理
score1 = 90
score2 = 70
score3 = 60
score4 = 50
score5 = 80
#化為列表（用「中括號」將資料們包起來）
scores = [90,70,60,50,80]
#(序數)      0  1  2  3  4
print(scores)
#存放字串
friends = ["小黑","小黃","小綠"]
print(friends)
#存放不同資料型態
things = [90,"小黑",True]
print(things)

#取得列表中之內容 print(列表名稱[序數])
print(scores[0])
#取得倒數第一位(序數用-1，不是-0，-0算0)
print(scores[-1])
#取得列表中一個範圍的資料 print(列表名稱[起始序數:最後序數（不含）])
print(scores[0:2])
print(scores[1:4])
#從 第幾個資料 取到 最後一個資料 print(列表名稱[起始序數:])
print(scores[1:])
#從 第一個資料 取到 第幾個個資料 print(列表名稱[:最後序數（不含）])
print(scores[:4])

phrase = "Hello Mr.White"
#         01234567
print(phrase[0:5])
print(phrase[6:])

#列表中資料替換 變數名稱[要被改之資料之序數] = 新值
scores[0] = 30
print(scores)

#列表函式
#延伸列表中資料 .extend()
scores.extend(friends)
print(scores)
#增加（從後面）列表中資料 .append()
scores.append(30)
print(scores)
#在列表中插入值 .insert(要插入的位置,要插入的值)
scores.insert(2,40)
print(scores)
#在列表中移除值 .remove() （有相同的值的話，只會移除列表中第一個）
scores.remove(30)
scores.remove("小黑")
print(scores)
#移除列表的最後一位 .pop() （括弧內不需要傳入值）
scores.pop()
print(scores)
#讓列表中資料以升冪排序 .sort() （括弧內不需要傳入值）
scores.remove("小黃")
scores.remove("小綠")
scores.sort()
print(scores)
#把列表做反轉 .reverse （括弧內不需要傳入值）
scores.reverse()
print(scores)
#顯示想要找的值在列表中的位置 .index(想要找的值)
print(scores.index(70))
#.index()會回傳第一個找到的值的位置
scores = [90,70,70,50,80]
print(scores.index(70))
#數列表中有幾個該資料 .count(想要數有幾個的資料)
print(scores.count(70))
print(scores.count(7))
#清除列表中所有資料，使其變成空列表 .clear() 括弧內不需要傳入值
scores.clear()
print(scores)