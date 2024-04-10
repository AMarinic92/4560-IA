# How to run
This file contains instructions on how to run the socket

## Packages
- python-dotenv
- asyncio
- socketio

## Install Instructions
We use web sockets to connect asynchronously our backend and frontend because WebSockets are more persistent than regular and have more direct support 
1. Create a .env file in the socket folder and create the variables USERNAME(your username where the cluster is) ,HOST(domain name) & CLUSTER_HOST (cluster ip address) , and give them the values of your gallium login
2. Create socket on HOST by running python3 socket/server.py 
3. Forward port on HOST to your local host by running portForward.py on your local computer , this should bind both ports

