from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Site(BaseHTTPRequestHandler):
    def do_GET(self):

        html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="utf-8">
    <title>شرکت تسدیگی</title>

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
        راه نفس رو بغضِ بیدادِ تو میگیره
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