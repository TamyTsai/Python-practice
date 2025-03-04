# 標準函式庫—網路與網頁操作

import urllib.request # 引入Python標準函式庫含有的urllib.request模組
# 這個模組提供操作 URL 的工具，包括發送 HTTP 請求和處理響應。
# urllib 適合簡單的 HTTP 請求，如果需要更多功能（如處理 cookies 或 POST 請求），建議使用第三方庫，例如 requests

# 取得伺服器回傳
response = urllib.request.urlopen("https://www.example.com") # 呼叫urllib.request模組的urlopen函式
# 使用 urllib.request.urlopen() 方法發送一個 HTTP GET 請求到指定的 URL（https://www.example.com）
# 函式回傳一個包含 伺服器響應的對象，存入變數response

# 讀取 伺服器回傳對象 的HTML內容（二進制格式）
html = response.read()
# 從 response 對象中 讀取 伺服器 回傳 的內容，並將之指定給 變數 html
# html 是一個二進制格式的資料（bytes），包含了網頁的 原始 HTML 內容

# 以指定編碼方式解碼 二進制格式的HTML內容
print(html.decode('utf-8'))
# 使用 decode('utf-8') 將 二進制格式的 html 內容解碼為 UTF-8 編碼的字符串
# 將解碼後的 HTML 內容輸出到控制台