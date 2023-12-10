#!/usr/bin/python3
import subprocess
import datetime
import pytz

OUTPATH = "/home/michael/shared/out/"
PROCPATH = "/home/michael/shared/proc/"

def ffmpeg(infile):
    cmd = "ffmpeg -nostdin -hide_banner -i " + PROCPATH +"\"" + infile + "\" "
    cmd += "-filter_complex \"[0:0]pan=mono|c0=c0[left0]; [0:0]pan=mono|c0=c1[right0];  [0:1]pan=mono|c0=c0[left1]; "
    cmd += "[0:1]pan=mono|c0=c1[right1];  [0:2]pan=mono|c0=c0[left2]; [0:2]pan=mono|c0=c1[right2];  [0:3]pan=mono|c0=c0[left3]; "
    cmd += "[0:3]pan=mono|c0=c1[right3]; "
    cmd += "[left0][right0][left1][right1][left2][right2][left3][right3]amix=inputs=8:duration=longest:normalize=0\" -ac 1 "
    cmd += OUTPATH + "\"" + infile[:-4] + "-mono.mp3\" "
    cmd += "2>" + OUTPATH + "\"" + infile[:-4] + "-mono.log\""
    print("begin processing " + infile + " at " + str(datetime.datetime.now(pytz.timezone('America/Chicago'))))
#    print(cmd)
    output = subprocess.check_output(cmd, shell=True, text=True)
    print(str(output))
    print("end processing " + infile + " at " + str(datetime.datetime.now(pytz.timezone('America/Chicago'))))
#    output = "output stub"
    return(output)

def move(infile,outpath=OUTPATH):
    success = True
    cmdstr = "mv " + PROCPATH + "\"" + infile + "\" " + outpath
    try:
        subprocess.check_output(cmdstr, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.output); success = False
    return(success)
    
cmdstr = "ls -p " + PROCPATH + " | grep -v / | tr '\n' ',' | sed 's/.$//'"
output = subprocess.check_output(cmdstr, shell=True, text=True)
lines = output.split(",")

for line in lines:
    movefile = True
    filename = line.strip()
    if filename[-3:] == "m4a":
        fpresults = ffmpeg(filename)
        print(str(fpresults))
    elif len(filename) == 0:
        movefile = False

    if movefile == True:
        if move(filename) == True:
            dtmstamp = str(datetime.datetime.now(pytz.timezone('America/Chicago'))) + ": "
            print(dtmstamp + filename + " moved to " + OUTPATH)
