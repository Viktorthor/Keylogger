import platform
import subprocess

print(platform.platform())
print(platform.system())

if (platform.system() == "Linux" ):
    subprocess.call(['python', 'linux.py'])
else:
    subprocess.call(['python', 'windows.py'])


