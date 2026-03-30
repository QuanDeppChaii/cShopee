import random
import string
from pathlib import Path

GENERATED_DIR = Path("/tmp/generated")
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

def random_id(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_html_file(img, content, link):
    file_id = random_id()
    filename = f"{file_id}.html"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta property="og:title" content="{content}">
<meta property="og:description" content="{content}">
<meta property="og:type" content="website">

<meta property="og:image" content="{img}">
<meta property="og:image:secure_url" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<meta http-equiv="refresh" content="2; url={link}">
</head>
<body></body>
</html>
"""

    file_path = GENERATED_DIR / filename
    file_path.write_text(html, encoding="utf-8")

    return file_id
