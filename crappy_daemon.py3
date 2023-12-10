#!/usr/bin/python3
import subprocess
import datetime
import pytz
import time

BASEPATH = "/home/michael/shared/"

while True:
    cmdstr = BASEPATH +"probetest-v2.py3"
    dtmstamp = str(datetime.datetime.now(pytz.timezone('America/Chicago'))) + ": "
    print(dtmstamp + "running probetest")
    output = subprocess.check_output(cmdstr, shell=True, text=True)
    print("probetest output:")
    print(str(output))

    cmdstr = BASEPATH +"proctest-v1.py3"
    dtmstamp = str(datetime.datetime.now(pytz.timezone('America/Chicago'))) + ": "
    print(dtmstamp + "running proctest")
    output = subprocess.check_output(cmdstr, shell=True, text=True)
    print("proctest output:")
    print(str(output))
    
    time.sleep(60)
