from datetime import datetime
from io import BytesIO

from flask import Flask, jsonify, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)

IMAGE_WIDTH = 860
IMAGE_HEIGHT = 300

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/")
def api_page():
    return jsonify({
        'error': 'JSON'
    })


@app.route("/api/demo/black-square")
def api_demo_page():
    img = Image.new(mode="RGB", size=(250, 250))
    return serve_pil_image(img)


@app.route("/api/demo/text")
def api_demo_text_page():
    out = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))

    # get a font
    # fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)

    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text
    d.multiline_text((10, 10), "Hello\nWorld", fill=(0, 0, 0))

    today = datetime.today()
    d.multiline_text((10,50), today.strftime("%m/%d/%Y, %H:%M:%S"), fill=(0, 0, 0))

    return serve_pil_image(out)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
