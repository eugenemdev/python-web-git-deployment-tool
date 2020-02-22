# Python monitoring tool to build and deploy git code (in progress)

## Introduction

This python-script checks your Github repository and pulls new code to it. Next step is the building new code and starting or restarting NodeJS application. The script executes on the server. All operations execute every 10 minutes.

## History

Once I thought about some server script, that will be very useful to check the new changes from the Github cloud repository, make a new build and start or restart NodeJS server. I had a stable provider, but he reloaded my VPS server every day and in time, that I couldn't plane. So it was born the idea and concept, that was released by me here.

## How to use the code

***Step by step***

1. make clone this repository 
`git clone https://github.com/eugenemdev/python-web-git-deployment-tool.git`
2.  change dir /python-web-git-deployment-tool
`cd python-web-git-deployment-tool`
3. install packages
`npm install --save-dev`
4. - added python libs with command 
```pip3 install gitpython re json```
5. build frontend for monitor
`npm run build`

6. go to dir above. We need to clone [simple-test-server](https://github.com/eugenemdev/simple-test-server). Monitoring tool works by default settings with simple-test-server 
`cd ../`
7. make clone [simple-test-server](https://github.com/eugenemdev/simple-test-server)
`git clone https://github.com/eugenemdev/simple-test-server.git`
8.  change dir /simple-test-server
`cd simple-test-server`
9. install packages
`npm install --save-dev`
10. build simple application
`npm run build`

See config.py in dir /python-web-git-deployment-tool
watchDir - it's the directory which we will watch, by default 'simple-test-server'
start - it's name of server's file in dir /simple-test-server 

!!! It's very important to have right package.json in simple-test-server
by default in the part "scripts":

```
"scripts": {
    "start":"node server.js",
    "dev": "live-server src --verbose",
    "build": "webpack --mode production",
    "test": "echo \"Error: no test specified\" && exit 1"
```
so let's go:
11. change dir to ../python-web-git-deployment-tool
`cd ../python-web-git-deployment-tool`
12. start Python Server `python3 start.py`

 - see web monitor by http://localhost:3000
 - see worked simple-test-server by http://localhost:8081


***Later we will add the information  how to start this script as systemctl service in Linux and autoinstall bash script***

## [View the demo]() ... soon!
![screen of web tool](./screen.png)

## Author

- [Eugen Morozov](https://eugenmorozov.de)