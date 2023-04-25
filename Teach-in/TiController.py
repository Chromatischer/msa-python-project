#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from TouchStyle import *
from InputMethode import *
from TiModel import *
from TxtStickInput import *

inputMethode = InputMethode(["joystick"])


class TiController(QRunnable):
    def getJoystickInput(self):
        self.txtstinp = TxtStickInput(self.txt)
        if self.txtstinp.getPos("left", "X") != 0:
            while self.txtstinp.getPos("right", "X") != 0:
                self.tiModel.MovementAgent.DirectControl.Safe.m1(self.txtstinp.getPos("left", "X"))
        else:
            self.tiModel.MovementAgent.DirectControl.Safe.m1(0)


    @staticmethod
    def getFileInput():
        pass

    def __init__(self, value_txt: ftrobopy):
        super().__init__()

        self.txt = value_txt

        self.tiModel = TiModel(self.txt)

    def run(self):
        self.inputMethode: InputMethode

        print("entered main loop of TiController 100%")

        print("setting default config for txt:")
        # ConfigPy.set_default_config()

        print("testing motors!")
        self.tiModel.TestMotors.Counters.m1()
        self.tiModel.TestMotors.Reset.m1()
        print("test motor 1 complete!")
        self.tiModel.TestMotors.Counters.m2()
        self.tiModel.TestMotors.Reset.m2()
        print("test motor 2 complete!")
        self.tiModel.TestMotors.Counters.m3()
        self.tiModel.TestMotors.Reset.m3()
        print("test motor 3 complete!")
        self.tiModel.TestMotors.Counters.m4()
        self.tiModel.TestMotors.Reset.m4()
        print("test motor 4 complete!")

        while True:
            if inputMethode.getInputMethode() == "joystick":
                self.getJoystickInput()
            elif inputMethode.getInputMethode() == "file":
                self.getFileInput()
