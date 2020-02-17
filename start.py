#!/usr/bin/python3
# pip3 install gitpython

import git
import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
from datetime import datetime
import threading
import multiprocessing

# Initializing STATE
STATE = {
    "system" : {
        "name" : "Linux CentOS",
        "lastreboot" : ""
    },
    "repo" : {
        "name" : "", 
        "date" : "", 
        "status" : "",
        "previous_commit" : "",
        "last_commit" : "",
        "description" : "",
    },
    "build" : {
       "date" :  "", 
       "status" : "", 
       "description" : "", 
    },
    "deploy" : {
        "date" : "", 
        "status" : "", 
        "description" : "" 
    }
}

# current directory, where is the script 
gitDirectory = os.getcwd()
#print (gitDirectory)
repo = git.Repo(gitDirectory)
STATE["repo"]["name"] = str(repo)

#get information about last commit
def getCommit():
    return repo.head.commit

def get_time_as_num():
    time = datetime.now() 
    #time = str(time)[11:13] + str(time)[14:16] HHMIN
    time = str(time)[15:16] # MIN LAST DIGIT
    return int(time)

# python job that starts every 10 minutes
def job():    
    time = get_time_as_num()
    print("Job Started in %s" %time)
    result  = getPull()

    if result == True:
        build()
    else: 
        print('Creation new build was passed')
    pass

def ticker():    
    start = 0 #option starts every 10 minutes
    print(get_time_as_num())
    timer = threading.Event()

    while True:
        time = get_time_as_num()
        print("timer awake in %s" %time)
        if time == start:            
            job()
            
        timer.wait(59.0)


# get pull to repository
def getPull():
    lastCommitBefore = getCommit()    
    git.cmd.Git(gitDirectory).pull    
    lastCommitAfter = getCommit()
    
    STATE["repo"]["previous_commit"] = str(lastCommitBefore)
    STATE["repo"]["last_commit"] = str(lastCommitAfter)

    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    STATE["repo"]["date"] = str(date_string)    

    if(lastCommitBefore != lastCommitAfter):        
        STATE["repo"]["status"] = "Passed"
        STATE["repo"]["description"] = "New code was pulled in to repository"
        logging.info("New code was pulled in to repository")         
        return True
    else:
        STATE["repo"]["status"] = "Passed"
        STATE["repo"]["description"] = "New pushes were not found"        
        logging.info("New pushes were not found ")
        return False
    
    data = STATE    

    with open("dist/state.json", "w") as write_file:
        json.dump(data, write_file)
        filename = gitDirectory + '/dist/state.json'

def build():
    newbuild = os.system('npm run build')    
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    STATE["build"]["date"] = str(date_string)
    STATE["build"]["status"] = "Passed"
    STATE["build"]["status"] = "Source was built successful"
    logging.info('Source was built successful')
    data = STATE

    with open("dist/state.json", "w") as write_file:
        json.dump(data, write_file)
        filename = gitDirectory + '/dist/state.json'

class MyHandler(BaseHTTPRequestHandler): 

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers() 
    
    def do_GET(self):        

        if self.path == '/getstate':  
            filename = gitDirectory + '/dist/state.json'    
        elif self.path == '/':
            filename = gitDirectory + '/dist/index.html'            
        else:
            filename = gitDirectory + '/dist/' + self.path

        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        
        self.send_response(200)

        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        with open(filename, 'rb') as fh:
            html = fh.read()            
            #html and other files
            self.wfile.write(html)


def runHTTPServer(server_class=HTTPServer, handler_class=MyHandler, port=3000):                
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


# when server start
if __name__ == "__main__":      
    proc1 = multiprocessing.Process(target=ticker)
    proc2 = multiprocessing.Process(target=runHTTPServer)
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()