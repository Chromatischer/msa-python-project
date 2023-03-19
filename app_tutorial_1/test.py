#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from TouchStyle import *


class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)
        # Creates an empty MainWindow
        w = TouchWindow("Test")

        try:
            txt = ftrobopy.ftrobopy('localhost', 65000)  # connect to TXT's IO controller
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
            button = QPushButton("Toggle O1")  # create a button labeled "Toggle O1"
            w.setCentralWidget(button)  # attach it to the main output area

            # configure all TXT outputs to normal mode
            M = [txt.C_OUTPUT, txt.C_OUTPUT, txt.C_OUTPUT, txt.C_OUTPUT]
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
            self.light_on = True  # remember that the light is on
            self.txt.setPwm(0, 512)  # set PWM to 512 (full on)

            self.timer = QTimer(self)  # create a timer
            self.timer.timeout.connect(self.on_timer)  # connect timer to on_timer slot
            self.timer.start(100)  # fire timer every 100ms (10 hz)

        w.show()
        self.exec_()

    def toggle_light(self):
        self.light_on = not self.light_on  # change state
        if self.light_on:  # set output accordingly
            self.txt.setPwm(0, 512)  # PWM=512 means full on
        else:
            self.txt.setPwm(0, 0)  # PWM=0 means off

    # an event handler for the timer (also a qt slot)
    def on_timer(self):
        self.toggle_light()


if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
