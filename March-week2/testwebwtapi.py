from http.server import BaseHTTPRequestHandler, HTTPServer
import quandl
mydata = quandl.get("FRED/GDP")
quandl.ApiConfig.api_key = "yoATsozuHyNEh7TyW5iH"
print(mydata)
print(type(mydata))
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #message="done it"
        message = str.encode(mydata)
        self.wfile.write(bytes(message, "utf8"))
        return
def run():
    print('starting server...')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()
run()
