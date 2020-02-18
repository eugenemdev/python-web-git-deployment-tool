
# need to check that pgrep is working in the terminal
import os
import logging
import json
import multiprocessing
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def killServer():
    os.system('pkill node')
    logging.warning('Node Server was stopped')

def startServer():
    os.system('node simple-server.js')    
    logging.warning('Node Server was started')

def check():
    pid = os.system('pgrep node') #return pid   #pgrep -v -u root #all processes
    if str(pid) == '256': # Out == 256 when proccess in system doesn't exist
        logging.warning('Node Server is down')
        return pid
    else: 
        logging.info('Node Server works')
        return pid

def deploy(STATE, gitDirectory):

    pid = check()
    proccessNodeServer = multiprocessing.Process(target=startServer)
    
    if str(pid) == '256':        
        proccessNodeServer.start()        
    elif str(pid) != '256':
        killServer()
        #proc3.close() # when we kill the proccess before than it need not to close after
        proccessNodeServer.start()

    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    STATE["deploy"]["date"] = str(date_string)
    STATE["deploy"]["status"] = "Passed"
    STATE["deploy"]["description"] = "NodeJS server started successfuly"
    
    logging.info('Source was deployed successful')
    
    data = STATE

    with open("dist/state.json", "w") as write_file:
        json.dump(data, write_file)
        filename = gitDirectory + '/dist/state.json'