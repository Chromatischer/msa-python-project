#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import ftrobopy
from ftrobopy import *


class SimpleTxtConnector:

    def __init__(self, direct=False):
        self.txt = None
        if direct:
            try:
                print("trying to connect to direct")
                self.txt = ftrobopy('direct', use_extension=True)

            except (TimeoutError, ConnectionRefusedError, NameError) as error:
                print("failed to connect to direct: ", error)
        else:
            if not self.txt:
                try:
                    print("trying to connect to offline USB mode")
                    self.txt = ftrobopy('192.168.7.2', use_extension=True)

                except (TimeoutError, ConnectionRefusedError) as error:
                    print("failed to connect to offline USB mode: ", error)

            if not self.txt:
                try:
                    print("trying to connect to localhost")
                    self.txt = ftrobopy('localhost', use_extension=True)

                except (TimeoutError, ConnectionRefusedError) as error:
                    print("failed to connect to localhost: ", error)

            if not self.txt:
                try:
                    print("trying to connect to W-lan host")
                    self.txt = ftrobopy('192.168.178.72', use_extension=True)

                except (TimeoutError, ConnectionRefusedError) as error:
                    print("failed to connect to W-lan host: ", error)

        if not self.txt:
            raise ConnectionRefusedError("cant connect to txt!")
        else:
            self.txt: ftrobopy

    #   if not self.txt.getPower() > 7900:
    #       raise OSError("input voltage to low! Switch battery immediately!")
    #   else:
    #       print(self.txt.getPower())
