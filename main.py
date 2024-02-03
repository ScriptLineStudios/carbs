import json
import utils

from flask import Flask, request, send_file, render_template
import asyncio

app = Flask(__name__)
loop = asyncio.get_event_loop()
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = json.loads(request.data)
    code = data.get("code")
    lang = data.get("lang")
    theme = data.get("theme", "material")
    pv = data.get("pv", 0)
    ph = data.get("ph", 0)
    font = data.get("font", "Hack")
    font_size = data.get("font_size", 14)
    window_theme = data.get("window_theme", "sharp")
    window_controls = data.get("window_controls", True)
    
    if not lang or utils.invalid_lang(lang):
        return utils.error("Please include a language!")
    if code:
        code = utils.clean_code(code)
    else:
        return utils.error("Please include your code!")

    url = f"https://carbon.now.sh/?wc={str(window_controls).lower()}&wt={window_theme}&fm={font}&fs={font_size}px&l={lang}&t={theme}&pv={pv}px&ph={ph}px&es=2x&code={code}"
    # image = utils.screenshot(url, driver)
    image = utils.screenshot(url)

    return send_file(image), 200

if __name__ == "__main__":
    app.run(host="", port=5000, debug=True)

