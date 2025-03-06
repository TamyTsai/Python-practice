# 模組的使用

import my_module # 將my_module.py檔案（模組）引入
# import 其他python檔案名稱（不用加副檔名）
# 不含副檔名的檔案名稱 即為模組的名稱

# 使用模組中的功能
# 想取模組中某一變數的值---print（檔案名.變數名）
# 想使用模組中某一函式---print（檔案名.函式名(參數)）
print(my_module.greet("Alice")) # 使用模組中的函式
print(my_module.MY_PI) # 使用模組中的變數
print(my_module.circle_area(5))