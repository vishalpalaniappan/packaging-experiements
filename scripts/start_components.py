import subprocess

def startDb():

    print("Starting database...")

    cmd = ["docker", "ps", "-aq", "-f", "name=asp-mariadb"]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )

    if (len(output.stdout) > 0):
        subprocess.run(
            ["docker", "start", "asp-mariadb"],
            capture_output=True, 
            text=True
        )
    else:
        cmd = [
            "docker", "run",\
            "-d",\
            "--name", "asp-mariadb",\
            "-v", "./data/mariadb:/var/lib/mysql", \
            "-e", "MYSQL_ROOT_PASSWORD=random-password", \
            "-e", "MYSQL_DATABASE=asp-database", \
            "-p", "3306:3306", \
            "mariadb:latest" \
        ]
        subprocess.run(cmd)

    print("Started database on port 3306.")

if __name__ == "__main__":
    startDb()