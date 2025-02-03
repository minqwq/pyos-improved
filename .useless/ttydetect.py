import subprocess
ttymode = "null"
def is_tty():
    result = subprocess.run(["sh", "-t"], capture_output=True)
    if result.returncode == 0:
        ttymode = True
    else:
        ttymode = False

if ttymode == True:
    print("RUnning on tty unknown")
elif ttymode == False:
    pass
