import subprocess

def doesContainerExist(name):
    cmd = ["docker", "ps", "-aq", "-f", f"name={name}"]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )

    return len(output.stdout) > 0

def doesImageExist(name):
    cmd = ["docker", "image", "inspect", name]
    output = subprocess.run(
        cmd, 
        capture_output=True, 
        text=True
    )

    return len(output.stdout) > 0

def buildDocker(imageName, dockerPath, srcPath):

    if not doesImageExist(imageName):
        subprocess.run([
            "docker",
            "build",
            "-t",
            imageName,
            "-f",
            dockerPath,
            srcPath
        ])