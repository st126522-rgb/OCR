import pytesseract
from PIL import Image
import os

def executeOCR(image, config=r'--psm 7 -l nep_dev_script3 --tessdata-dir "C:\Users\User2\Desktop\NepOCR\tesseract_model\Best"', T_exe_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
    # Set the Tesseract executable path
    pytesseract.pytesseract.tesseract_cmd = T_exe_path
    
    # Parse the config to find the tessdata directory and set the TESSDATA_PREFIX environment variable
    config_parts = config.split()
    for i, part in enumerate(config_parts):
        if part == '--tessdata-dir':
            print(os.environ['TESSDATA_PREFIX'])
            tessdata_dir = config_parts[i + 1].strip('"')
            os.environ['TESSDATA_PREFIX'] = tessdata_dir
            print(os.environ['TESSDATA_PREFIX'])
            break
    
    # Perform OCR using pytesseract
    try:
        text = pytesseract.image_to_string(image, config=config)
        if not text:
            return "Could not read text"
        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    img_path = r"test_images\DevaTest2.png"
    config = r'--psm 7 -l nep_sl --tessdata-dir "C:\Users\User2\Desktop\NepOCR\tesseract_model\Custom"'
    loaded_image = Image.open(img_path)
    txt = executeOCR(image=loaded_image, config=config)
    print(txt)
    # with open("abcd.txt", "w", encoding="utf-8") as file:
    #     file.write(txt)
