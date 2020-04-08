import platform
import subprocess
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
import os.path

###############
# The main script to run
# Usable on Linux and Windows
# Calls the corresponding script with usage from the platform package
###############
if (platform.system() == "Linux" ):
    subprocess.call(['python', 'linux.py'])
else:
    subprocess.call(['python', 'windows.py'])
