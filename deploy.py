
# need to check that pgrep is working in the terminal
import os
import logging
import json
import multiprocessing
from datetime import datetime
import config
import store


class Deploy:

    logging.basicConfig(level=logging.INFO)
    State = store.Store()

    def __inet__(self):
        self.State = State
    
    def killServer(self, pid):
        #os.system('pkill node')
        os.system('kill -9 %s' %pid)
        logging.warning('Node Server was stopped')

    def startServer(self):
        command = "npm run start --prefix " + "../" + config.watchDir
        os.system(command)
        logging.warning('Node Server was started')

    def check(self):
        #pid = os.system('pgrep node') #return pid   #pgrep -v -u root #all processes
        pid = os.system("ps aux | grep node| grep %s | awk '{print $2}'" %config.start)        
        return pid

    def deploy(self):

        proccessNodeServer = multiprocessing.Process(target=self.startServer)
        pid = self.check()        
    
        if pid == 0:
            logging.warning('Node Server is down')        
            proccessNodeServer.start()   
            logging.info('Node Server works')
        else:
            logging.info('Node Server reloads')
            self.killServer(pid)
            #proc3.close() # when we kill the proccess before than it need not to close after
            proccessNodeServer.start()

        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
        self.State.set("deploy", "date", str(date_string))
        self.State.set("deploy", "status", "Passed")
        self.State.set("deploy", "description", "NodeJS server started successfuly")
    
        logging.info('Source was deployed successful')