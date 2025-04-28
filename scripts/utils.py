import subprocess

def containerExists(name):
    cmd = ["docker", "ps", "-aq", "-f", f"name={name}"]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )

    return len(output.stdout) > 0

def buildDocker(imageName, dockerPath, srcPath):
    subprocess.run([
        "docker",
        "build",
        "-t",
        imageName,
        "-f",
        dockerPath,
        srcPath
    ])