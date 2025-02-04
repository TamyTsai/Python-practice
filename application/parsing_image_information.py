# 解析圖檔資訊
from PIL import Image

def get_image_specs(file_path):
	try: # 若檔案無法開啟或不存在，將引發 FileNotFoundError，進入後續的 except 區塊
		# 使用 Pillow 打開影像檔案
		with Image.open(file_path) as img: # 打開位於file_path路徑上的檔案，並將之存入img變數
			# 擷取影像屬性
			specs = {
				"Width": img.width, # 讀取img物件width屬性的值
				"Height": img.height,
				"Format": img.format
			}
			return specs
	# 捕捉可能的例外，例如檔案不存在（FileNotFoundError）或其他未預期的錯誤
	except FileNotFoundError:
		print(f"檔案未找到：{file_path}")
	except Exception as e:
		print(f"發生錯誤：{e}")
		
# 測試程式
file_path = "/content/drive/My_Drive/test_image/IMG_8102.jpg" # 影像檔的路徑
specs = get_image_specs(file_path)
if specs: # 若成功解析
	print("影像規格：", specs)