from urllib.parse import quote
from uuid import uuid4
from pathlib import Path

GENERATED_DIR = Path("generated")
GENERATED_DIR.mkdir(exist_ok=True)

def create_html_file(img, content, link):
    filename = f"{uuid4()}.html"
    encoded = quote(link, safe="")

    html = f"""<!DOCTYPE html>
<html lang="en">
  <head>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TF9MWHH7');</script>
<!-- End Google Tag Manager -->
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ââ Xuáº¥t hiá»n Äoáº¡n clip ghi láº¡i cáº£nh....</title>
    <meta content="âNÃNG: Xuáº¥t hiá»n Äoáº¡n clip ghi láº¡i cáº£nh..." property="og:title">
    <meta content="âNÃNG: Xuáº¥t hiá»n Äoáº¡n clip ghi láº¡i cáº£nh..." property="og:description">
    <meta content="NEWS" property="og:type">

    <!-- THUMBNAIL FACEBOOK -->
    <meta property="og:image" content="https://dantri.live/ok/okok.png">
    <meta property="og:image:secure_url" content="https://dantri.live/ok/okok.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta content="Logo Facebook" property="og:image:alt">

    <script>
    setTimeout(function() {
        window.location.href = "https://shopee.vn/unilevervn_beauty?uls_trackid=52nbl188001e&utm_campaign=id_jQ4gIpmAP6&utm_content=----&utm_medium=affiliates&utm_source=an_17369960334&utm_term=d1e2hd2rbais"; // Chuyá»n hÆ°á»g sau 500ms
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
"""

    file_path = GENERATED_DIR / filename
    file_path.write_text(html, encoding="utf-8")

    return filename
