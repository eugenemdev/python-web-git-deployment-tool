# Which repository you will watch,
# save this repo in one dir with python-web-git-deployment-tool dir
watchDir = "simple-test-server"

#name of script to start with NodeJS server
start = "server.js"

Pairs = [
            (".css", "'Content-type', 'text/css'"), 
            (".json", "'Content-type', 'application/javascript'"), 
            (".js", "'Content-type', 'application/javascript'"),
            (".ico", "'Content-type', 'image/x-icon'"),
            (".html" , "'Content-type', 'text/html'")
        ]

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