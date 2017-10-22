# validcode.py
# 根据图片返回验证码

from PIL import Image
from pytesseract import image_to_string
from io import BytesIO

def initTable(threshold=130):
 	table = []
 	for i in range(256):
 		if i < threshold:
 			table.append(0)
 		else:
 			table.append(1)
 	return table


#利用tesseract-ocr将验证码识别为字符串
def validcode(imgContent):
	im = Image.open(BytesIO(imgContent))
	im = im.convert('L')
	binaryImage = im.point(initTable(), '1')
	# binaryImage.show()
	code = image_to_string(binaryImage,config = '-psm 7')
	print(code)
	return code

