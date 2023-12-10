#!/usr/bin/python3
import subprocess
import datetime
import pytz

INPATH = "/home/michael/shared/in/"
OUTPATH = "/home/michael/shared/out/"
PROCPATH = "/home/michael/shared/proc/"

def ffprobe(infile):
    cmdstr = "ffprobe " + INPATH +"\"" + infile + "\" 2>&1 | grep -E \"JAVS|Stream\s\#\""
    output = subprocess.check_output(cmdstr, shell=True, text=True)
    return(output)

def move(infile,outpath=OUTPATH):
    success = True
    cmdstr = "mv " + INPATH + "\"" + infile + "\" " + outpath
    try:
        subprocess.check_output(cmdstr, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.output); success = False
    return(success)
    
cmdstr = "ls -p " + INPATH + " | grep -v / | tr '\n' ',' | sed 's/.$//'"
output = subprocess.check_output(cmdstr, shell=True, text=True)
lines = output.split(",")

for line in lines:
    movefile, outpath = True, OUTPATH
    filename = line.strip()
    if filename[-3:] == "m4a":
        fpresults = ffprobe(filename)
        if fpresults.find('JAVS') > -1:
            info = "stream_info: "
            i = fpresults.find('Stream #')
            while i > -1:
                info += fpresults[i+8:i+11] + " "
                i = fpresults.find('Hz, ',i)
                info += fpresults[i+4:i+8] + "|"
                i = fpresults.find('Stream #',i)
            if info.find("0:0 ster|0:1 ster|0:2 ster|0:3 ster") > -1:
                outpath = PROCPATH
    elif len(filename) == 0:
        movefile = False

    if movefile == True:
        if move(filename,outpath) == True:
            dtmstamp = str(datetime.datetime.now(pytz.timezone('America/Chicago'))) + ": "
            print(dtmstamp + filename + " moved to " + outpath)
