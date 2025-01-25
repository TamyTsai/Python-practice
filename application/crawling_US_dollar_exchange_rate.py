# 第三方函式庫—網頁爬蟲

import requests # 引入第三方函式庫requests
from bs4 import BeautifulSoup # 從 第三方函式庫bs4 引入 BeautifulSoup模組
# 第三方函式庫要先透過pip install來安裝（但colab已經有預裝常見的）
# requests: 用於發送 HTTP 請求並接收回應（如 HTML）
# BeautifulSoup: 來自 bs4 模組，用於解析和提取 HTML 文件中的內容

def fetch_usd_to_twd_rate(): # 定義一個名為 fetch_usd_to_twd_rate 的函式，無需參數，用於從指定網站抓取美元兌台幣的匯率

	url = "https://rate.bot.com.tw/xrt?Lang=zh-TW" # 臺灣銀行匯率網頁URL
	
	try:
		# 發送GET請求取得網頁內容
		response = requests.get(url) # 使用 requests.get(url) 發送 HTTP GET 請求，將回應存入變數 response
		response.raise_for_status() # response.raise_for_status(): 檢查請求是否成功（HTTP 狀態碼為 200），如果不是，則引發異常（跳到except敘述區塊）
		
		# 使用BeautifulSoup解析HTML
		soup = BeautifulSoup(response.text, 'html.parser') # 使用 BeautifulSoup 將 回應的 HTML 文本 解析為 Python 可操作的結構，指定解析器為 'html.parser'
		# html parser 解析網頁的標籤語言
		# 變數 soup 是解析後的 HTML 文件
		
		# 找到匯率表格
		table = soup.find('tbody') # 使用 soup.find('tbody') 查找 HTML 中的 <tbody> 元素（匯率數據通常位於 <tbody> 中）
		if not table: # 如果 table 為 None（未找到 <tbody>），則輸出錯誤訊息並返回
			print("找不到匯率表格")
			return
		
		# 找到美元的表格行
		usd_row = None # 初始化 usd_row 為 None，用於存儲美元匯率的表格行
		for row in table.find_all('tr'): # 使用 table.find_all('tr') 遍歷所有表格行（<tr>）
			currency_td = row.find('td', {'date-table': '幣別'}) # 每行中，使用 row.find('td', {'data-table': '幣別'}) 查找該行的 "幣別" 欄位
			if currency_td and '美金' in currency_td.text: # 如果找到該欄位，且其內容包含 "美金"
				usd_row = row # ，則將該行存入 usd_row
				break # 並停止迴圈
		
		if not usd_row: # 如果 usd_row 為 None，表示未找到美元匯率的相關行
			print("找不到美元的匯率資料") # 則輸出錯誤訊息
			return # 並回傳
		
		# 找到「本行現金買入」匯率
		cash_buy_rate = usd_row.find('td', {'date-table': '本行現金買入'}).text.strip()
		# 在 usd_row 中查找 <td> 標籤，屬性 data-table 為 '本行現金買入'，代表現金買入匯率
		# 提取該欄位的文字內容，並使用 .strip() 去除前後多餘空白
		
		print(f"目前美元對台幣的現金匯率（本行買入）：{cash_buy_rate} TWD") # 使用格式化字串輸出美元對台幣的現金買入匯率
	
	# 在發生異常時，輸出錯誤訊息
	except requests.exceptions.RequestException as e: # 第一個 except 捕獲與 HTTP 請求相關的異常（如無法連線、超時）
		print(f"無法獲取匯率資料：{e}")
	except Exception as e: # 第二個 except 捕獲其他可能的異常（如 HTML 結構變更導致解析失敗）
		print(f"解析網頁時發生錯誤: {e}")
		
# 網址改變 或 網頁內容 調整 就可能會出錯

# 呼叫（執行）函數
fetch_usd_to_twd_rate()
