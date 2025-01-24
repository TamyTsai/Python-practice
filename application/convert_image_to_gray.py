# 第三方函式庫—影像處理

from google.colab import drive # 從google.colab第三方函式庫 引入 drive模組
drive.mount('/content/drive') # 呼叫 drive 模組的 mount函式
# 掛載雲端硬碟

import cv2 # 引入第三方函式庫 cv2
import os # 引入Python標準函式庫含有的os模組

file_path = '/content/drive/My_Drive/test_image'

# 讀取照片
image = cv2.imread(f'{file_path}IMG_8102.jpg') # 呼叫cv2第三方函式庫 的 imread函式
# imread：image read
# 將讀取到的照片 指定給 image變數

# 轉換為灰階影像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 呼叫cv2第三方函式庫 的 cvtColor函式 及 COLOR_BGR2GRAY函式
# cvtColor：convert color
# 將轉為灰階的影像 指定給 gray_image變數

# 保存結果
cv2.imwrite(f'{file_path}IMG_8102_gray.jpg', gray_image)
# 使用 imwrite() 函式，可以將處理好的資料內容寫入並儲存為圖片
# imwrite() 有三個參數，第一個參數為檔案的路徑和名稱，第二個參數為要寫入的資料內容，第三個參數為圖片壓縮品質的設定 ( 非必要，參考：ImwriteFlags )