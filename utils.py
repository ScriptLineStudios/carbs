import json
from selenium.webdriver.common.by import By
import time
from PIL import Image
import io
import urllib.parse
import random

def screenshot(url, driver):
    driver.get(url)

    image_binary = driver.find_element(By.XPATH, '//*[@id="export-container"]').screenshot_as_png 
    img = Image.open(io.BytesIO(image_binary))
    
    filename = f"images/image_{random.randrange(0, 100000)}.png"
    img.save(filename)

    return filename

def invalid_lang(lang):
    return False

def error(msg):
    return json.dumps({"Error": msg}), 404

def clean_code(code):
    return urllib.parse.quote(code)
