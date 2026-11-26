# Vista previa local: python servir.py  ->  abre http://localhost:8000
import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as s:
    webbrowser.open("http://localhost:8000"); s.serve_forever()
