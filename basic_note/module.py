# 模組module的使用（python的檔案）
# import 其他python檔案名稱（不用加副檔名）
# 想取模組中某一變數的值---print（檔案名.變數名）
# 想使用模組中某一函式---print（檔案名.函式名(參數)）

#python內建模組（python module list）
# import 模組名稱

import token
import sys
#尋找該模組所在的路徑
print(sys.path)
#lib是存放內建模組之處

# 第三方模組
# pip 套件管理工具
# 終端機輸入：pip install numpy 就會開始安裝
# 縮寫
improt numpy as np
# as 可取別名，之後要取 模組中 某一變數的值---print（檔案名.變數名），檔案名（套件）就可以用 別名 寫
