# 讀取二進位檔案

import struct #  引入 struct 模組，用於解析二進位格式的數據（例如 JPEG 標頭 中以 二進位 儲存的 長度 和 尺寸 資訊）。

def parse_jpg_header(file_path): # 宣告名為parse_jpg_header之函式，用於解析指定 JPEG 檔案的 標頭 並 提取 影像尺寸 等資訊
	try: # 若檔案無法開啟或不存在，將引發 FileNotFoundError，進入後續的 except 區塊
		with open(file_path, "rb") as file: # 對路徑位於file_path的檔案 使用「二進位讀取檔案」模式 ，並將檔案存入file變數
		# 使用with語法，在檔案操作完成後會自動關閉
			# 驗證檔案是否為 JPEG 格式
			file_type = file.read(2) # 讀取檔案的前兩個位元組，這是 JPEG 檔案的 起始標記（Start of Image, SOI）
			if file_type != b'\xFF\xD8': # JPEG檔的起始標記（SOI）
				raise ValueError("檔案不是正確的JPEG格式") # 如果標記不符，拋出 ValueError，說明檔案不是有效的 JPEG 格式
			
			# 進入解析循環 逐步解析 JPEG 標頭
			while True:
				# 讀取標記（Marker）
				marker, = struct.unpack(">H", file.read(2))
				# read(2)：二進位底下，這樣寫，代表要讀取兩個位元組
				# file.read(2): 讀取兩個位元組，這些是 JPEG 的 段標記（Marker）
				# unpack：將格式拆開 解包
				# struct.unpack(">H", file.read(2)): 使用 大端（>）格式 解析為 16 位元整數（H），表示段標記
				
				# 檢查是否為 SOF0 或其他 SOF 標記
				# 判斷標記是否是 SOF0（Baseline DCT） 或 SOF2（Progressive DCT），這些標記包含影像的 寬與高 資訊
				if marker in (0xFFC0, 0xFFC2): # SOF0（基線 DCT） 或 SOF2（進階DCT）
					file.read(3) # 跳過 段長度（2 位元組）和精度（1 位元組）。
					height, width = struct.unpack(">HH", file.read(4)) # 讀取影像 高度 與 寬度，各佔 2 位元組
					# 使用 大端格式 解析 兩個 無符號 短整數（H），分別為 高度 和 寬度
					return {"Width": width, "Height": height, "Format": "JPEG"}
				
				# 讀取段長度，移動到下一段
				segment_length, = struct.unpack(">H", file.read(2)) #  讀取段長度（2 位元組）
				file.seek(segment_length - 2, 1) # 跳過該段的內容，segment_length - 2 是扣除段長度本身的 2 位元組
	
	# 捕捉可能的例外，例如檔案不存在（FileNotFoundError）或其他未預期的錯誤
	except FileNotFoundError:
		print(f"找不到這個檔案：{file_path}")
	except Exception as e:
		print(f"發生錯誤：{e}")

# 測試程式
jpeg_file = "/content/drive/My_Drive/test_image/IMG_8102.jpg" # JPEG檔的路徑
specs = parse_jpg_header(jpeg_file)
if specs: # 如果變數的值不為None，0，空字符串，空列表，空字典（=若成功解析）
	print("JPEG資訊：", specs) # 則輸出影像資訊（例如寬度與高度）
					