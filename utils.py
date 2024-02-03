import json
import time
import io
import urllib.parse
import random
from pyppeteer import launch

# def screenshot(url, driver):
#     driver.get(url)

#     image_binary = driver.find_element(By.XPATH, '//*[@id="export-container"]').screenshot_as_png 
#     img = Image.open(io.BytesIO(image_binary))
    
#     filename = f"images/image_{random.randrange(0, 100000)}.png"
#     img.save(filename)

#     return filename

async def open_carbonnowsh(url):
    browser = await launch(defaultViewPort=None,
                           handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False,
                           headless=True,
                           args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': "images"
    })
    await page.goto(url, timeout=100000)
    return browser, page


async def screenshot(url):
    browser, page = await open_carbonnowsh(url)
    element = await page.querySelector("#export-container  .container-bg")
    path = f"images/image_{random.randrange(0, 100000)}.png"
    img = await element.screenshot({'path': path})
    await browser.close()
    return (path)

def invalid_lang(lang):
    return False

def error(msg):
    return json.dumps({"Error": msg}), 404

def clean_code(code):
    return urllib.parse.quote(code)
