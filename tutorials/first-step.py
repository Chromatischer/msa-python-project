#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from TouchStyle import *

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        global txt
        global posM1, posM2, posM3, posM4

        TouchApplication.__init__(self, args)
        # Creates an empty MainWindow
        w = TouchWindow("Test")

        try:
            txt = ftrobopy.ftrobopy('ft-txt', 65000)  # connect to TXT's IO controller
        except:
            txt = None  # set TXT to "None" of connection failed

        if not txt:
            # display error if TXT could no be connected
            # error messages is centered and may span
            # over several lines
            err_msg = QLabel("could not connect to txt!")  # create the error message label
            err_msg.setWordWrap(True)  # allow it to wrap over several lines
            err_msg.setAlignment(Qt.AlignCenter)  # center it horizontally
            w.setCentralWidget(err_msg)  # attach it to the main output area
        else:
            # initialization went fine. So the main gui
            # is being drawn

            # configure all TXT outputs to normal mode
            M = [txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR]
            I = [(txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL)]
            txt.setConfig(M, I)
            txt.updateConfig()
            txt.getCurrentCounterInput(0)
            print("first", txt.getCurrentCounterValue(0))
            self.SaveMove.m1(self, 1)
            print(txt.getCurrentCounterValue(0))
            txt.updateWait(1)
            print(txt.getCurrentCounterValue(0))
            txt.stopAll()

            # self.timer = QTimer(self)  # create a timer
            # self.timer.timeout.connect(self.on_timer)  # connect timer to on_timer slot
            # self.timer.start(500)  # fire timer every 500ms (2 hz)

        w.show()
        self.exec_()

    class SaveMove():
        def m1(self, dist):
            if dist > 0:
                print(txt.getCurrentCounterValue(0))
                txt.setPwm(1, 256)


if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
