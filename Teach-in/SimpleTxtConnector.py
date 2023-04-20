#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ftrobopy import *


class SimpleTxtConnector:

    def __init__(self):
        self.txt: ftrobopy
        try:
            print("trying to connect to localhost")
            self.txt = ftrobopy('localhost', 65000, False, True)

        except (TimeoutError, ConnectionRefusedError) as error:
            print("failed to connect to localhost: ", error)
            self.txt = None

        if not self.txt:
            try:
                print("trying to connect to W-lan host")
                self.txt = ftrobopy('ft-txt', 65000)

            except (TimeoutError, ConnectionRefusedError) as error:
                print("failed to connect to W-lan host: ", error)
                self.txt = None

        if not self.txt:
            raise ConnectionRefusedError("cant connect to txt!")
        else:
            self.txt: ftrobopy

    #   if not self.txt.getPower() > 7900:
    #       raise OSError("input voltage to low! Switch battery immediately!")
    #   else:
    #       print(self.txt.getPower())
