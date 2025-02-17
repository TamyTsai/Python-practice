# 資料夾相關指令

import os 
current_dir = os.getcwd() # cwd：current working directory
# 取得當前目錄位置
list_file = os.listdir(current_dir) # listdir：連隱藏檔都可以印出來
# 列出 當前目錄 中 所含有的 目錄或檔案
# 回傳值為串列
print(f"目前的資料夾為：{current_dir}")
print(f"目前資料夾內的資料有：{list_file}")
# ./ 路徑即是指目前的資料夾
print(f"資料夾 ./ 內的資料有：{os.listdir('./')}")
# 以上兩行敘述執行結果相同