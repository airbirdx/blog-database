import subprocess
import datetime
import sys
from cnblog import *


if len(sys.argv) == 2:
    info = str(sys.argv[1])
else:
    info = "auto push at " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M %p'))

auto_cnblog()

# print('-------------------------------------------')
# print('---> git status ---------------------------')
# print('-------------------------------------------')
subprocess.call(["git", "status"])

# print('-------------------------------------------')
# print('---> git add . ----------------------------')
# print('-------------------------------------------')
subprocess.call(["git", "add", "."])

# print('-------------------------------------------')
# print('---> git commit -m info -------------------')
# print('-------------------------------------------')
subprocess.call(["git", "commit", "-m", info])

# print('-------------------------------------------')
# print('---> git pull origin master ---------------')
# print('-------------------------------------------')
subprocess.call(["git", "pull", "origin", "master"])

# print('-------------------------------------------')
# print('---> git push -u origin master ------------')
# print('-------------------------------------------')
subprocess.call(["git", "push", "-u","origin", "master"])

print('\n')
print('-------------------------------------------')
print('---> D.O.N.E ------------------------------')
print('-------------------------------------------')