import subprocess
import datetime
import sys

if len(sys.argv) == 2:
    info = str(sys.argv[1])
else:
    info = "auto push at " + str(datetime.datetime.now())

subprocess.call(["git", "status"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", info])
subprocess.call(["git", "pull", "origin", "master"])
subprocess.call(["git", "push", "-u","origin", "master"])
