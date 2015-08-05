#!/usr/bin/python3

##
# This will act as a wrapper for curses so that we can
# implement it into our board.
##

import curses

class graphics:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(True)

    def stop(self):
        """Execute controlled tear down of curses."""
        curses.nocbreak()
        curses.curs_set(1)
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
