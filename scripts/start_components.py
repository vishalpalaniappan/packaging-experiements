import subprocess
from utils import doesContainerExist, buildDocker
from constants import *

def buildImages():

    buildDocker(
        QUERY_IMAGE_NAME,
        "docker-images/query-server/Dockerfile",
        "components/query-server/"
    )

    buildDocker(
        ASV_IMAGE_NAME,
        "docker-images/asv/Dockerfile",
        "components/asv/"
    )

    buildDocker(
        DLV_IMAGE_NAME,
        "docker-images/dlv/Dockerfile",
        "components/dlv/"
    )


def startQueryServer():
    '''
        Starts the query server.
    '''
    print("Starting Query Server...")
    if (doesContainerExist(QUERY_CONTAINER_NAME)):
        subprocess.run(["docker", "start", QUERY_CONTAINER_NAME])
    else:
        cmd = [
            "docker", "run",\
            "-d",\
            "--name", "asp-query-server-container",\
            "-p", "8765:8765", \
            QUERY_IMAGE_NAME \
        ]
        subprocess.run(cmd)

    print("Started Query Server on port 8765.")

def startASV():
    '''
        Starts the automated system viewer container.
    '''

    print("Starting asv...")
    if (doesContainerExist(ASV_CONTAINER_NAME)):
        subprocess.run(["docker", "start", ASV_CONTAINER_NAME])
    else:
        cmd = [
            "docker", "run",\
            "-d",\
            "--name", ASV_CONTAINER_NAME,\
            "-p", "3011:3011", \
            "-v", "./data/asv:/app/dist", \
            ASV_IMAGE_NAME \
        ]
        subprocess.run(cmd)
    print("Started asv on port 3011.")

def startDLV():
    '''
        Starts the diagnostic log viewer container.
    '''

    print("Starting dlv...")    
    if (doesContainerExist(DLV_CONTAINER_NAME)):
        subprocess.run(["docker", "start", DLV_CONTAINER_NAME])
    else:
        cmd = [
            "docker", "run",\
            "-d",\
            "--name", DLV_CONTAINER_NAME,\
            "-p", "3011:3011", \
            "-v", "./data/dlv:/app/dist", \
            DLV_IMAGE_NAME \
        ]
        subprocess.run(cmd)
    print("Started dlv on port 3011.")

def startDB():
    '''
        Starts the diagnostic database container.
    '''

    print("Starting database...")
    if (doesContainerExist(DATABASE_CONTAINER_NAME)):
        subprocess.run(["docker", "start", DATABASE_CONTAINER_NAME])
    else:
        cmd = [
            "docker", "run",\
            "-d",\
            "--name", DATABASE_CONTAINER_NAME,\
            "-v", "./data/mariadb:/var/lib/mysql", \
            "-e", "MYSQL_ROOT_PASSWORD=random-password", \
            "-e", "MYSQL_DATABASE=asp-database", \
            "-p", "3306:3306", \
            DATABASE_IMAGE_NAME \
        ]
        subprocess.run(cmd)
    print("Started database on port 3306.")

if __name__ == "__main__":
    buildImages()
    startASV()
    startDB()
    startDLV()
    startQueryServer()