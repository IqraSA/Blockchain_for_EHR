#try:
from PIL import Image
#except ImportError:
 #   import Image
import pytesseract

def ocr_core(images):
    """
    This function will handle the core OCR processing of images.
    """
    return pytesseract.image_to_string(Image.open(images))

print(ocr_core('sample1.jpg'))