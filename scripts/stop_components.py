import subprocess
from constants import *

def stopDb():

    print("Stopping query server...")
    cmd = ["docker", "stop", QUERY_CONTAINER_NAME]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )    
    print("Stopped query server service.")

    print("Stopping ASV...")
    cmd = ["docker", "stop",  ASV_CONTAINER_NAME]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )    
    print("Stopped ASV service.")

    print("Stopping DLV...")
    cmd = ["docker", "stop",  DLV_CONTAINER_NAME]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )    
    print("Stopped DLV service.")

    print("Stopping database...")
    cmd = ["docker", "stop",  DATABASE_CONTAINER_NAME]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )
    print("Stopped database service.")

if __name__ == "__main__":
    stopDb()