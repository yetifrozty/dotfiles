#!/usr/bin/python3
import sys
import time
import os



def truncate(string, width):
    if len(string) > width:
        string = string[:width-3] + '...'
    return string

#print(truncate("awdawdawdawd", 5))

def run(command):
    with os.popen(command) as cmd:
        return cmd.read()
lockpid = run('cat ~/.config/polybar/media.lock')
#print(int(lockpid))
curpid = os.getpid()

for pid in run('pgrep media.py').splitlines():
    #print(pid, pid==int(lockpid))
    if int(pid) == int(lockpid):
        os.system(f'kill {lockpid}')
os.system(f'echo {curpid} > ~/.config/polybar/media.lock')

for line in sys.stdin:
    line = line.rstrip("\n").replace("Playing", "").replace("Paused", "契")
    songinfo = line[line.rfind("怜") + 6:].replace("\"", "")

    #line = truncate(line, 20).rstrip('\n')
    line = line[:line.rfind("怜") + 6] + truncate(songinfo, 25)
    #print(line)
    os.system(f"echo '{line}' > ~/.config/polybar/curmedia")
    pids = run('pgrep polybar').splitlines()
    for pid in pids:
        os.system(f'polybar-msg -p {pid} hook media 1 &>/dev/null')
        


