CRAPPY DAEMON

The crappy_daemon.py3 script is meant to control the two subscripts.

The probetest-v2.py3 script monitors an IN directory for new files. If the files are M4A, it probes them to see if they fit the profile. If they do, they get moved to the PROC folder. Otherwise, they get moved to the OUT folder.

The proctest-v1.py3 script grabs a list of M4A files in the PROC directory, and applies the defined FFMpeg process to them. The resulting MP3 is created in the out folder, and the FFMPeg output is also logged in the OUT folder. The original file is then moved to the OUT folder as well
