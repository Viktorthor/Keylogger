import platform
import subprocess
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
import os.path


if (platform.system() == "Linux" ):
    subprocess.call(['python', 'linux.py'])
else:
    subprocess.call(['python', 'windows.py'])
