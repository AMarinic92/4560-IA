# portFoward
# forwards port 5000 from the cluster asynchronously which should be a socket 
import os
from dotenv import load_dotenv
import asyncio

load_dotenv() 


host = os.getenv("HOST")

username = os.getenv("USERNAME")

cluster_ip = os.getenv("CLUSTER_HOST")



async def main():
   ssh_forwarding = await asyncio.create_subprocess_shell(
        f'ssh -L {5001}:{cluster_ip}:5000 {username}@{host} '
    )
   await ssh_forwarding.wait()


asyncio.run(main())