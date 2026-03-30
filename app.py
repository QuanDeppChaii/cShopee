from flask import Flask, render_template, request, send_from_directory
from pathlib import Path
from generator import create_html_file

app = Flask(__name__)

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

    file_id = create_html_file(image_url, content, shopee_url)

    link = f"/{file_id}"
    return render_template("form.html", link=link)

@app.route("/<file_id>")
def open_file(file_id):
    filename = f"{file_id}.html"
    return send_from_directory(GENERATED_DIR, filename)
