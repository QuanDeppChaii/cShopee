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

    html = '''<!DOCTYPE html>
<html lang="en">
  <head>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TF9MWHH7');</script>
<!-- End Google Tag Manager -->
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
<!-- End Google Tag Manager -->
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'''+content+'''</title>
    <meta content="'''+content+'''" property="og:title">
    <meta content="'''+content+'''" property="og:description">
    <meta content="NEWS" property="og:type">

    <!-- THUMBNAIL FACEBOOK -->
    <meta property="og:image" content="'''+img+'''">
    <meta property="og:image:secure_url" content="'''+img+'''">
    <meta property="og:image:secure_url" content="'''+img+'''">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta content="Logo Facebook" property="og:image:alt">

    <script>
    setTimeout(function() {
        window.location.href = "'''+link+'''"; // Chuyá»n hÆ°á»g sau 500ms
    }, 500); // Ä»£i 500ms trÆ°á» khi chuyá»n trang
    </script>

  </head>
  <body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TF9MWHH7"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
  </body>
  </html>
'''
    file_path = GENERATED_DIR / filename
    file_path.write_text(html, encoding="utf-8")
    return file_id
