#!/usr/bin/python3
# pip3 install gitpython

import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
from datetime import datetime
import threading
import multiprocessing

import build
import gitcmds
import deploy
import handler
import config

# Initializing STATE
STATE = config.STATE

gitDirectory = gitcmds.getGitDirectory()
repo = gitcmds.getRepo(gitDirectory)
STATE["repo"]["name"] = str(repo)

def get_time_as_num():
    time = datetime.now()             
    #time = str(time)[11:13] + str(time)[14:16] HHMIN
    time = str(time)[15:16] # MIN  LAST DIGIT

    #for testing 
    #time = str(time)[17:19] # SEC LAST DIGIT  
    return int(time)


# python job that starts every 10 minutes
def job():    
    
    time = get_time_as_num()    
    result  = gitcmds.getPull(STATE, gitDirectory, repo)    

    if result == True:
        build(STATE, gitDirectory)
        deploy.deploy(STATE, gitDirectory)
    else: 
        logging.info('There aren\'t new changes to build new release')
        result = deploy.check()
        if result == 256:
            deploy.deploy(STATE, gitDirectory)

    # for testing
    #build.build(STATE, gitDirectory)
    #deploy.deploy(STATE, gitDirectory)
    
    pass

def ticker():    
    start = 0 #option starts every 10 minutes    
    timer = threading.Event()
    
    while True:
        time = get_time_as_num()
        logging.info("Timer woke up in %s min." %time)
        if time == start:            
            job()
            
        timer.wait(59.0) #sec

def runHTTPServer(server_class=HTTPServer, handler_class=handler.MyHandler, port=3000):                
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()        


# when server start
if __name__ == "__main__":
    try:      
        proccess1 = multiprocessing.Process(target=ticker)
        proccess2 = multiprocessing.Process(target=runHTTPServer)
        proccess1.start()
        proccess2.start()
        proccess1.join()
        proccess2.join()
    except KeyboardInterrupt:
        proccess1.terminate()
        logging.info('Stopping timer...\n')
        proccess2.terminate()
        logging.info('Stopping httpd...\n')
        