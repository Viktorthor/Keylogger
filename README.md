# Keylogger

## Viktors & Ómars Keylogger

#### You can download the repo and we recommend using virtualenv. To do so make sure you have virtualenv installed and follow these steps:
* Setting up virtual env
    * 1. virtualenv -p python3 virtualenv
    * 2. source VENV/bin/activate
    * 3. pip install -r requirements.txt

Please note the instructions can be varying due to different operating systems.

## Usage :
 To use the keylogger after setting up VENV simply run:
*python keylogger.py*

Keylogger.py checks what kind of OS is running on the machine and selects the corresponding subprocess, whether it be linux.py or windows.py.  

Then the corresponding subprocess activates the keylogger function and instantly starts by creating a log and entering the users keystrokes. Alongside that the scheduler begins counting down to the set interval (default 12 hours) to send the log via email. You can change the email to receive and send in the code, it's easy to find if you follow the comments. Once sent, the log will be erased from the local directory and starts a new one marking each log with a time and date stamp alongside the local computers username.

### Note :
The logger will run until the local computer is either shutdown or via keyboard interrupt (Ctrl+C) in the terminal where the program is running.

#### Sidenote :
Keyboard interrupt is not functioning on the windows side of the keylogger. To exit the program simply close the terminal or end the python task in your task manager.


## Final assignment for Computer System Security
This program is created as part of a final assignment in the class "Computer System Security" at the University of Iceland. Reasons for keylogging are either for security purposes for a company, whether they be seeing what staff is up to or how their people are interacting on the computers or for attackers to try and grab sensitive information such as log-in information or other sensitive data. This program simply grabs every keystroke entered on the keyboard then sends the log file via e-mail every 12 hours. Functional on both Linux and Windows.

## Made by :
Ómar Þór Arnarsson & Viktor Þór Freysson  
otha3@hi.is & vthf1@hi.is
