import subprocess

def stopDb():

    print("Stopping database...")

    cmd = ["docker", "stop",  "asp-mariadb"]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )

    print("Stopped database service.")

if __name__ == "__main__":
    stopDb()