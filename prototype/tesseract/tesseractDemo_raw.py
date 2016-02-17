'''
Tesseract OCR Demonstration - Raw Input
Sample application to demonstrate capabilities of the Tesseract OCR API.
Baseline comparison of OCR techniques used without any kind of preprocessing involved.
'''

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# Perform OCR
result = pytesseract.image_to_string(Image.open('../../data/sample1.jpg'))

# Write out results to textfile
text_file = open("result/tesseractDemo_raw_result.txt", "w")
text_file.write(result)
text_file.close()

# TODO: Perform some type of analysis based on matched characters
