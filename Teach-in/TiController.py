#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from TouchStyle import *
from InputMethode import *
from TiModel import *

inputMethode = InputMethode("joystick")

txt = None
tiModel = None


class TiController(QRunnable):
    @staticmethod
    def getJoystickInput():
        pass

    @staticmethod
    def getFileInput():
        pass

    def __init__(self, value_txt: ftrobopy):
        super().__init__()
        global txt, tiModel

        txt: ftrobopy
        txt = value_txt

        tiModel: TiModel
        tiModel = TiModel(txt)

    def run(self):
        global inputMethode, txt, tiModel
        inputMethode: InputMethode

        print("entered main loop of TiController 100%")

        print("setting default config for txt:")
        ConfigPy.set_default_config()

        print("testing motors!")
        tiModel.TestMotors.m1()
        print("test motor 1 complete!")
        tiModel.TestMotors.m2()
        print("test motor 2 complete!")
        tiModel.TestMotors.m3()
        print("test motor 3 complete!")
        tiModel.TestMotors.m4()
        print("test motor 4 complete!")

        while True:
            if inputMethode.getInputMethode() == "joystick":
                self.getJoystickInput()
            elif inputMethode.getInputMethode() == "file":
                self.getFileInput()
