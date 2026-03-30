from urllib.parse import quote
from uuid import uuid4
from pathlib import Path

GENERATED_DIR = Path("/tmp/generated")
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

def create_html_file(img, content, link):
    filename = f"{uuid4()}.html"
    encoded = quote(link, safe="")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{content}</title>

<meta property="og:title" content="{content}">
<meta property="og:description" content="{content}">
<meta property="og:type" content="NEWS">

<meta property="og:image" content="{img}">
<meta property="og:image:secure_url" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<meta property="al:ios:url" content="shopeevn://reactPath?navigate_url={encoded}&path=shopee%2FTRANSFER_PAGE&version=1">
<meta property="al:ios:app_store_id" content="959841449">
<meta property="al:ios:app_name" content="Shopee VN">

<meta property="al:android:url" content="shopeevn://reactPath?navigate_url={encoded}&path=shopee%2FTRANSFER_PAGE&version=1">
<meta property="al:android:package" content="com.shopee.vn">
<meta property="al:android:app_name" content="Shopee VN">

<meta http-equiv="refresh" content="0; url={link}">

<script>
setTimeout(function(){{
    window.location.replace("{link}");
}}, 100);
</script>
</head>
<body></body>
</html>
"""

    file_path = GENERATED_DIR / filename
    file_path.write_text(html, encoding="utf-8")
    return filename
