# bmi計算器與錯誤處理
try:
  height = int(input("請輸入你的身高（公分）"))
  weight = int(input("請輸入你的體重（公斤）"))
  bmi = weight/(height/100)**2
except ZeroDivisionError as err: # 分母為零的錯誤處理
  print(f"身高不得為0，錯誤原因：{err}") # 用f搭配大括弧，來處理變數與字串的串接
except ValueError as err: # 數值錯誤的錯誤處理
  print("不得輸入非數字，錯誤原因",err) # 用課程講義中逗號的方式，來處理變數與字串的串接
except: # 通用錯誤處理，用來捕捉漏網之魚
  print("輸入有誤")
else: # 沒出錯的時候
  print(f"你的BMI是{bmi}")

# 閏年判斷
year = int(input("請輸入今年的西元年：")) # 取得使用者的輸入，並將其轉換為整數資料型態
is_leap_year = (year % 400)== 0 or ((year % 4 == 0) and (year % 100 !=0))
# 判斷是不是400的倍數（除以400時，餘數為0） 或是 雖是4的倍數（除以4時，餘數為0），但非100的倍數（除以100時，餘數非0）
# 用or邏輯運算子，就可以在其一條件成立時，即回傳True
# 用and邏輯運算字，就要在所有條件皆成立時，才會回傳True
print(f"今年是{year}年，是閏年嗎？{is_leap_year}") # 以f搭配大括弧，來串接字串與變數
# JavaScript ES6 是用 `${}`來串接字串與變數
# Ruby是用 #{} 來串接字串與變數