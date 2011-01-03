#!/usr/bin/python
'''
author:Shane Dowling
date:29/12/10

Python CLI-Dash, for presenting system information via the cli
'''

CONFIG_FILE = "conf_example"
CONFIG_DELIM = "||"

import curses
import cmdrunner
from cmdrunner import *

def main():

    run = cmdRunner()
    f = open(CONFIG_FILE, 'r')
    lines = f.readlines()
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    x_cord = 0
    for line in lines:
        x_cord = x_cord + 2
        cmds = line.strip().split(CONFIG_DELIM)
        process = ''
        for command in cmds:
            cmd, arg = command.split('(\'')
            arg = arg[:-2]
            res_cmd = run.resolve_func(cmd)
            if arg:
                process += run.do_command(res_cmd, arg) + "||"
            else:
                process += run.do_command(res_cmd) + "||"
        screen.addstr(x_cord, 5, process) 

    screen.addstr(x_cord+2, 5, "q - Exit")
    screen.refresh()
    x = screen.getch()
    curses.endwin()

    
    while x != ord('q'):
        pass

    curses.endwin()

if __name__ == "__main__":
    main();
