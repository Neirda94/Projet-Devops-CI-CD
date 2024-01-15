import http.server

def httpServer():
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", 8000), handler) as httpd:
        print("serving at port", 8000)
        httpd.serve_forever()