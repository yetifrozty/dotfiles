#!/usr/bin/env python3
import os

def run(command):
    with os.popen(command) as f:
        return f.read()

def workspace(monitors):
    amount = len(monitors)
    workspaces= " ".join(str(e) for e in list(range(1, 10//amount+1)))
    return workspaces
monitors = run(r"xrandr |awk '/connected/{print $1,$2}' | grep '\bconnected\b' | sed 's/ connected//g'").splitlines()
workspaces = workspace(monitors)

for monitor in monitors:
    run(f'bspc monitor {monitor} -d {workspaces}')