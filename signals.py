#signal.py

import signal, sys

def SigAlarmHandler(signal,frame):
    print('Received alarm.... Shutting down...')
    sys.exit(0)

signal.signal(signal.SIGALRM, SigAlarmHandler)
signal.alarm(20)

print('Start work... waiting for alarm to quit :)')
while True:
    #do something
    pass