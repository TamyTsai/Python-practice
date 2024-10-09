# 類別class、物件object
class Phone: #表示創建手機這個物件需要的資料 self物件
    def _init_(self,os,number,is_waterproof): #_init_表示初始函式 self表示物件本身
        self.os = os #物件有一個屬性叫os，而這個屬性被傳入os這個值
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)

#取得屬性資料
print(phone1.number)
# -->123
