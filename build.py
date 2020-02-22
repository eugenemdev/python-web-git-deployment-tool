
import os
import logging
import json
from datetime import datetime
import store
import config

logging.basicConfig(level=logging.INFO)

class Build:
    def __init__(self):
        self.State = store.Store()

    def build(self):
        command = "npm run build --prefix " + "../" + config.watchDir
        os.system(command)                
        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.State.set("build", "date", str(date_string))
        self.State.set("build", "status", "Passed")
        self.State.set("build", "description", "Source was built successful")        
    
        logging.info('Source was built successful')