import json
import time
import io
import urllib.parse
import random

from playwright.sync_api import sync_playwright

def screenshot(url):
    path = f"images/image_{random.randrange(0, 100000)}.png"
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(url)
        page.locator("#export-container  .container-bg").screenshot(path=path)
        browser.close()
    return path

def invalid_lang(lang):
    return False

def error(msg):
    return json.dumps({"Error": msg}), 404

def clean_code(code):
    return urllib.parse.quote(code)
