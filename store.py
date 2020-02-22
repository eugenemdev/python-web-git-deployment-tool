import json
import config
import logging
import os

State = {
    "system" : {
        "name" : "",
        "lastReboot" : "",
        "gitDirectory" : "",
        "toolDirectory" : "",        
        "jsonFilePath" : "",        
        "test" : ""
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

class Store:      
    logging.basicConfig(level=logging.INFO)
    _singleton = None

    def __new__(cls, *args, **kwargs):  
        print("cls._singleton: ", cls._singleton)  
        if not cls._singleton:  
            print("Create New Statement")  
            cls._singleton = object.__new__(Store)  
        return cls._singleton  
    
    def __init__(self):
        self.State = State
        toolDirectory = str(os.getcwd())

        jsonFilePath = toolDirectory + "/dist/state.json"
        lastReboot = os.popen("who -b").read()
        systemName = os.popen("uname -srm").read()
        

        self.State["system"]["toolDirectory"] = toolDirectory
        self.State["system"]["jsonFilePath"] = jsonFilePath
        self.State["system"]["lastReboot"] = lastReboot
        self.State["system"]["name"] = systemName 
        
        logging.info("Instance created!")       
        
        with open(jsonFilePath, 'w') as file:
            json.dump(self.State, file)     
        
    def set(self, paramTag, paramName, parameter):        
        jsonFilePath = self.State["system"]["jsonFilePath"]
        self.State[paramTag][paramName] = parameter
        with open(jsonFilePath, 'w') as file:
            json.dump(self.State, file)

    def get(self, paramTag, paramName):
        StateDictionary = self.getState()
        return StateDictionary[paramTag][paramName]            

    def getState(self):              
        jsonFilePath = self.State["system"]["jsonFilePath"]
        with open(jsonFilePath, 'rb') as file:
            State = json.load(file)
            return State
        
    def print(self):
        print (json.dumps(self.State, indent=2, sort_keys=True))        




#s1 = Store()
#s2 = Store()
#s1.set("system", "test","it's all right")
#print(s1.get("system", "test"))
#s1.print()
#s2.print()
