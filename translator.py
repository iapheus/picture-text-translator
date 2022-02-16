from googletrans import Translator, constants
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '' #The file location of tesseract.exe will be written here

textInPicture = pytesseract.image_to_string(Image.open(''), lang='eng',config='-c page_separator='' ')

translator = Translator()

translation = translator.translate(textInPicture.lower() , dest="tr") # We've changed the text to lowercase because some language translations have an alphabet-related translation error.
print(f"{textInPicture}--> {translation.text}")

