from PIL import Image
import pytesseract

img=Image.open('D:\my_projects_new\BrainDump\services\img.jpg')

text = pytesseract.image_to_string(img)

print(text)







