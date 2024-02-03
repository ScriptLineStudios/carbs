import json
import utils

from flask import Flask, request, send_file
from selenium import webdriver

app = Flask(__name__)

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

@app.route("/generate", methods=["POST"])
def generate():
    code = request.form.get("code")
    lang = request.form.get("lang")
    theme = request.form.get("theme", "material")
    pv = request.form.get("pv", 0)
    ph = request.form.get("ph", 0)
    font = request.form.get("font", "Hack")
    font_size = request.form.get("font_size", 14)
    window_theme = request.form.get("window_theme", "sharp")
    window_controls = request.form.get("window_controls", True)
    
    if not lang or utils.invalid_lang(lang):
        return utils.error("Please include a language!")
    if code:
        code = utils.clean_code(code)
    else:
        return utils.error("Please include your code!")

    url = f"https://carbon.now.sh/?wc={str(window_controls).lower()}&wt={window_theme}&fm={font}&fs={font_size}px&l={lang}&t={theme}&pv={pv}px&ph={ph}px&es=2x&code={code}"
    image = utils.screenshot(url, driver)
    return send_file(image), 200

if __name__ == "__main__":
    app.run(host="", port=5000, debug=False)

