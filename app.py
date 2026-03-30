from flask import Flask, render_template, request, url_for, send_from_directory
from pathlib import Path
from generator import create_html_file

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

GENERATED_DIR = Path("/tmp/generated")
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

@app.route("/")
def index():
    return render_template("form.html", link=None)

@app.route("/create", methods=["POST"])
def create():
    image_url = request.form.get("image_url", "").strip()
    content = request.form.get("content", "").strip()
    shopee_url = request.form.get("shopee_url", "").strip()

    filename = create_html_file(image_url, content, shopee_url)
    link = url_for("generated_file", filename=filename, _external=True)
    return render_template("form.html", link=link)

@app.route("/generated/<path:filename>")
def generated_file(filename):
    return send_from_directory(GENERATED_DIR, filename)
