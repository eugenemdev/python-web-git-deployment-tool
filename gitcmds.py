import git
import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
from datetime import datetime
import threading
import multiprocessing

logging.basicConfig(level=logging.INFO)

#get information about last commit
def getCommit(repo):
    return repo.head.commit

def getGitDirectory():
    gitDirectory = os.getcwd()    
    return gitDirectory

def getRepo(gitDirectory):
    repo = git.Repo(gitDirectory)
    return repo

def getPull(STATE, gitDirectory, repo):
    
    lastCommitBefore = getCommit(repo)    
    git.cmd.Git(gitDirectory).pull    
    lastCommitAfter = getCommit(repo)
    
    STATE["repo"]["previous_commit"] = str(lastCommitBefore)
    STATE["repo"]["last_commit"] = str(lastCommitAfter)

    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    STATE["repo"]["date"] = str(date_string)    

    data = STATE    

    with open("dist/state.json", "w") as write_file:
        json.dump(data, write_file)
        filename = gitDirectory + '/dist/state.json'

    if(lastCommitBefore != lastCommitAfter):        
        STATE["repo"]["status"] = "changed"
        STATE["repo"]["description"] = "New code was pulled in to repository"
        logging.info("New code was pulled in to repository")         
        return True
    else:
        STATE["repo"]["status"] = "didn't changed"
        STATE["repo"]["description"] = "It's nothing to build"        
        logging.info("It's nothing to build")
        return False
    
    
