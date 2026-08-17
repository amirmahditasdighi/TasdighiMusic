from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Site(BaseHTTPRequestHandler):
    if self.path == "/music.mp3":
    try:
        with open("music.mp3", "rb") as file:
            music = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "audio/mpeg")
        self.send_header("Content-Length", str(len(music)))
        self.end_headers()
        self.wfile.write(music)

    except FileNotFoundError:
        self.send_error(404, "Music not found")

    return
    def do_GET(self):

        html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="utf-8">
    <title>متن اهنگ خونه پر از رنج سکوته وای دلم تنگه</title>

    <style>
        body {
            text-align: center;
            font-family: Tahoma;
        }

        h1 {
            font-size: 50px;
            line-height: 2;
        }
    </style>
</head>

<body>

    <h1>
        خونه پر از رنج سکوتِ وای دلم تنگه<br>
        گلهای باغچه پیش چشمم وای چه بی رنگه<br>
        گل توی گلدون باز دوباره داره میمیره<br>
        راه نفس رو بغضِ بیدادِ تو میگیره<br>
        روزی به چشم تو من بهترین بودم<br>
        عاشق ترین بودی عاشق ترین بودم<br>
        از آشیون دل کندن و رفتن که آسون نیست<br>
        در سینه عشق تازه پروردن که آسون نیست<br>
        روزی به چشم تو من بهترین بودم<br>
        عاشق ترین بودی عاشق ترین بودم<br>
        خونه پر از رنجِ سکوتِ وای دلم تنگه<br>
        گلهای باغچه پیشِ چشمم وای چه بی رنگه<br>
        گل توی گلدون باز دوباره داره میمیره<br>
        راه نفس رو بغضِ بیدادِ تو میگیره<br>
        روزی به چشمِ تو من بهترین بودم<br>
        عاشق ترین بودی عاشق ترین بودم<br>
        از آشیون دل کندن و رفتن که آسون نیست<br>
        در سینه عشقِ تازه پروردن که آسون نیست<br>
        روزی به چشمِ تو من بهترین بودم<br>
        عاشق ترین بودی عاشق ترین بودم
    </h1>

</body>
</html>"""

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.end_headers()

        self.wfile.write(html.encode("utf-8"))


server = HTTPServer(
    ("0.0.0.0", int(os.environ.get("PORT", 8000))),
    Site
)

print("سایت اجرا شد")
server.serve_forever()
