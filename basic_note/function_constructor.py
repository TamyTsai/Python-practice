# 物件函式
class Phone: #表示創建手機這個物件需要的資料 self物件
    def _init_(self,os,number,is_waterproof): #_init_表示初始函式 self表示物件本身
        self.os = os #物件有一個屬性叫os，而這個屬性被傳入os這個值
        self.number = number
        self.is_waterproof = is_waterproof
    
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    
    def add(self,number1,number2):
        return number1 + number2

phone1 = Phone("ios",123,True)
print(phone1.is_ios())
print(phone1.add(5,6))

# 類別中 還能再定義 其他 函式
