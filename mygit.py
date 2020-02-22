import git 
import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
from datetime import datetime
import config
import store

class MyGit:
    logging.basicConfig(level=logging.INFO)

    def __init__(self):        
        self.State = store.Store()
        self.Repo = ""
        self.setGitDirectory()
        self.setRepo()        

    def getCommit(self):
        repo = self.Repo        
        commit = repo.head.commit        
        return commit

    def setGitDirectory(self):
        toolDirectory = os.getcwd()    
        self.State.set("system", "toolDirectory",  toolDirectory)
                    
        dir = toolDirectory.split('/')[:-1]
        dir.insert(len(dir), config.watchDir)
        gitDirectory = '/'.join(dir)            

        self.State.set("system", "gitDirectory", gitDirectory)
        return gitDirectory

    def setRepo(self):
        gitDirectory = self.State.get("system", "gitDirectory")        
        repo = git.Repo(gitDirectory)
        self.Repo = repo
        self.State.set("repo", "name", str(repo))

    def getPull(self):
        repo = self.Repo
        gitDirectory = self.State.get("system", "gitDirectory")
        toolDirectory = self.State.get("system","toolDirectory")

        commitBefore = self.getCommit()         
        git.cmd.Git(gitDirectory).pull    
        commitAfter = self.getCommit()
    
        self.State.set("repo", "previous_commit", str(commitBefore))
        self.State.set("repo", "last_commit", str(commitAfter))

        now = datetime.now()
        date_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.State.set("repo", "date", str(date_string))

        if(commitBefore != commitAfter):                                
            self.State.set("repo", "status", "changed")
            self.State.set("repo", "description", "New code was pulled in to repository")
            logging.info("New code was pulled in to repository")         
            return True
        else: 
            self.State.set("repo", "status", "didn't changed")
            self.State.set("repo", "description", "It's nothing to build")
            logging.info("It's nothing to build")
            return False
