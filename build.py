
import os
import logging
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def build(STATE, gitDirectory):
    
    newbuild = os.system('npm run build')    
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    STATE["build"]["date"] = str(date_string)
    STATE["build"]["status"] = "Passed"
    STATE["build"]["description"] = "Source was built successful"
    
    logging.info('Source was built successful')
    
    data = STATE

    with open("dist/state.json", "w") as write_file:
        json.dump(data, write_file)
        filename = gitDirectory + '/dist/state.json'