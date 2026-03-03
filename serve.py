import os, sys
os.chdir("/Users/fabianwillisimon/Documents/VD Wireframes")
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler).serve_forever()
