#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from TouchStyle import *

class FtcGuiApplication(TouchApplication):
    global M
    global I

    def __init__(self, args):
        global txt
        TouchApplication.__init__(self, args)
        # Creates an empty MainWindow
        w = TouchWindow("Test")

        try:
            txt = ftrobopy.ftrobopy('ft-txt', 65000)  # connect to wireless txt controller
        except:
            try:
                txt = ftrobopy.ftrobopy('localhost', 65000)  # connect to own txt controller port
            except:
                txt = None
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
            self.timer = QTimer(self)  # create a timer
            self.timer.timeout.connect(self.on_timer)  # connect timer to on_timer slot
            self.timer.start(500)  # fire timer every 500ms (2 hz)

            self.on_timed_event_executor = QTimer(self)
            self.on_timed_event_executor.timeout.connect(self.on_timed_execution)
            self.on_timed_event_executor.start(1)



        w.show()
        self.exec_()

    def on_timer(self):
        m1 = txt.motor(1)
        print("m1 distance:", m1.getCurrentDistance())
        print("m1 counter:", txt.getCurrentCounterValue(0))

    def on_timed_execution(self):
        Manager.SaveMove.m1(self, 1)


class Manager():
    class SaveMove():
        def m1(self, dist):
            if dist > 0:
                m1 = txt.motor(1)
                m1.setSpeed(-512)
            elif dist < 0:
                m1 = txt.motor(1)
                m1.setSpeed(100)


if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
