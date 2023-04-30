#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import termios
import ftrobopy


class TiView:

    def __init__(self, txt: ftrobopy):
        self.ttysettings = termios.tcgetattr(sys.stdin)
        print("TERMIOS initialized...")

    @staticmethod
    def update():
        pass

    def __delete__(self):
        print("TERMIOS resetting...")
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.ttysettings)
