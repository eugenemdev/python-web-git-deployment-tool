from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
import mygit
import re
import config
import store

logging.basicConfig(level=logging.INFO)


class MyHandler(BaseHTTPRequestHandler): 

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers() 
    
    def do_GET(self):
        
        Store = store.Store()

        toolDirectory = Store.get("system", "toolDirectory")
        jsonFilePath = Store.get("system", "jsonFilePath")


        if self.path == '/getstate':            
            filename = jsonFilePath    
        elif self.path == '/':
            filename = toolDirectory + '/dist/index.html'            
        else:
            filename = toolDirectory + '/dist/' + self.path        
        
        self.send_response(200)

        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        
        pairs = [
            (".css", "'Content-type', 'text/css'"), 
            (".json", "'Content-type', 'application/javascript'"), 
            (".js", "'Content-type', 'application/javascript'"),
            (".ico", "'Content-type', 'image/x-icon'"),
            (".html" , "'Content-type', 'text/html'")
        ]

        for fileType, contentHeader in pairs:                        
            
            result = bool(re.match(fileType, filename))                                  
            
            if result == True :                
                self.send_header(contentHeader)
            self.end_headers()
        
        with open(filename, 'rb') as file:
            html = file.read()                        
            self.wfile.write(html)
