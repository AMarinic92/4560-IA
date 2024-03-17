# Network Strategy

The network strategy involves using persistent socket connection using the web socket implementation . This done by using socket io on both the chrome extension and on a port on the cluster .  

## Step 1
Send a message to the socket server at the cluster as a json object {"website":"url"} . When the socket receives the message it starts parsing the website and generating a relevant response.


## Step 2 
The socket server on the cluster then responds with a json object with appropriate suggestions to improve alt text .
