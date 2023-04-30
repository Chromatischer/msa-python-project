#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import ftrobopy
import curses

class TiView:

    def __init__(self, txt: ftrobopy):
        self.screen = curses.initscr()
        curses.noecho()
        pass

    @staticmethod
    def update():
        pass
