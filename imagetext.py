from PIL import Image
from pytesseract import image_to_string

img1 = Image.open('/home/bikumalla/Pictures/rivereffect.png')
text1 = image_to_string(img1,lang='eng')
print(text1)

print(" ")

img2 = Image.open('/home/bikumalla/Pictures/rivereffect2.jpg')
text2 = image_to_string(img2)
print(text2)

