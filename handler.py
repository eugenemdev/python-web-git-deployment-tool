from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
import gitcmds
import re

logging.basicConfig(level=logging.INFO)


class MyHandler(BaseHTTPRequestHandler): 

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers() 
    
    def do_GET(self):

        gitDirectory = gitcmds.getGitDirectory()

        if self.path == '/getstate':  
            filename = gitDirectory + '/dist/state.json'    
        elif self.path == '/':
            filename = gitDirectory + '/dist/index.html'            
        else:
            filename = gitDirectory + '/dist/' + self.path        
        
        self.send_response(200)
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        pairs = [
            (".css", "'Content-type', 'text/css'"), 
            (".json", "'Content-type', 'application/javascript'"), 
            (".js", "'Content-type', 'application/javascript'"),
            (".ico", "'Content-type', 'image/x-icon'"),
            (".html" , "'Content-type', 'text/html'")
        ]

        for a, b in pairs:                        
            result = bool(re.match(a, filename))                      
            if result == True :                
                self.send_header(b)
            self.end_headers()
        
        with open(filename, 'rb') as fh:
            html = fh.read()                        
            self.wfile.write(html)
