# Python monitoring tool to build and deploy git code (In progress)

## Introduction

This python-script checks your Github repository and pulls new code to it. Next step is the building new code and starting or restarting NodeJS application. The script executes on the server. All operations execute every 10 minutes.

## History

Once I thought about some server script, that will be very useful to check the new changes from the Github cloud repository, make a new build and start or restart NodeJS server. I had a stable provider, but he reloaded my VPS server every day and in time, that I couldn't plane. So it was born the idea and concept, that was released by me here.

## Using the code

- make clone this repository 
```git clone https://github.com/eugenemdev/python-web-git-deployment-tool.git```
- see config.py and fix directory own Repo, that will be monitoring    
- build frontend files for web monitoring:  `npm run build`
- added python libs with command ```pip3 install gitpython re json```
- start Python Server `python3 start.py`
- see web monitor by http://localhost:3000

***Later will be adding the information about how to start this script as systemctl service in Linux System***

## [View the demo]() ... soon!
![screen of web tool](./screen.png)

## Author

- [Eugen Morozov](https://eugenmorozov.de)