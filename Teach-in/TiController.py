#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from TouchStyle import *
from InputMethode import *
from TiModel import *
from TiPosition import *
from TxtStickInput import *


inputMethode = InputMethode(["joystick"])
tipos: [TiPosition] = []


class TiController(QRunnable):
    def getJoystickInput(self):
        if self.txtstinp.getButton("left"):
            tipos.append(TiPosition(self.tiModel.getCounterValue(1), self.tiModel.getCounterValue(2), self.tiModel.getCounterValue(3), self.tiModel.getCounterValue(4)))
            print("left button press! ", tipos[len(tipos)-1].get_str())
            self.txt.updateWait(0.7)

        if self.txtstinp.getButton("right"):
            inputMethode.setInputMethode("file")

        if self.txtstinp.getPos("right", "Y") != 0:
            while self.txtstinp.getPos("right", "Y") != 0:
                if self.verbose: print("right, Y -> ", -round(self.txtstinp.getPos("right", "Y")))
                self.tiModel.MovementAgent.DirectControl.Safe.m1(-self.txtstinp.getPos("right", "Y"))
        else:
            self.tiModel.MovementAgent.DirectControl.Safe.m1(0)

        if self.txtstinp.getPos("left", "Y") != 0:
            while self.txtstinp.getPos("left", "Y") != 0:
                if self.verbose: print("left, Y -> ", round(self.txtstinp.getPos("left", "Y")))
                self.tiModel.MovementAgent.DirectControl.Safe.m2(self.txtstinp.getPos("left", "Y"))
        else:
            self.tiModel.MovementAgent.DirectControl.Safe.m2(0)

        if self.txtstinp.getPos("right", "X") != 0:
            while self.txtstinp.getPos("right", "X") != 0:
                if self.verbose: print("right, X -> ", round(self.txtstinp.getPos("right", "X")))
                self.tiModel.MovementAgent.DirectControl.Safe.m4(self.txtstinp.getPos("right", "X"))
        else:
            self.tiModel.MovementAgent.DirectControl.Safe.m4(0)

        if self.txtstinp.getPos("left", "X") != 0:
            while self.txtstinp.getPos("left", "X") != 0:
                if self.verbose: print("left, X -> ", round(self.txtstinp.getPos("left", "X")))
                self.tiModel.MovementAgent.DirectControl.Safe.m3(self.txtstinp.getPos("left", "X"))
        else:
            self.tiModel.MovementAgent.DirectControl.Safe.m3(0)

    def getFileInput(self):
        # it is currently 25.Apr.23 at 22:00 I am ill because of my operation and I have take 600mg of Ibuprofen,
        # if I for some unknown reason wake up tomorrow, and this code works, I think I might just be Jesus!
        # I do NOT think, this code will work, like AT ALL it is going to not work very badly!
        #                                          did it work?:

        i = 0
        for tiPosition in tipos:
            i += 1
            if self.verbose:
                print("executing run for element: ", i, " in tipos with values: ", tiPosition.get_str())
            for m in range(4):
                if self.verbose:
                    print("element: ", i, " motor: ", m, " current value: ", self.tiModel.getCounterValue(m), " target: ", tiPosition.__getattr__(m))
                while self.tiModel.getCounterValue(m) < tiPosition.__getattr__(m):
                    if self.verbose:
                        print("current value smaller target, Direct-control set to 1")
                    #I have no clue what I am doing, nor have I gotten any Idea weather or not it will work!
                    to_exec: str = "self.tiModel.MovementAgent.DirectControl.Safe.m" + str(m) + "(1)"
                    exec(to_exec)

                while self.tiModel.getCounterValue(m) > tiPosition.__getattr__(m):
                    if self.verbose:
                        print("current value larger target, Direct-control set to -1")
                    #I have no clue what I am doing, nor have I gotten any Idea weather or not it will work!
                    to_exec: str = "self.tiModel.MovementAgent.DirectControl.Safe.m" + str(m) + "(-1)"
                    exec(to_exec)

                if self.verbose:
                    print("current value after run: ", self.tiModel.getCounterValue(m), " target was: ", tiPosition.__getattr__(m))

    def __init__(self, value_txt: ftrobopy, verbose=False):
        super().__init__()

        self.txt = value_txt

        self.tiModel = TiModel(self.txt)
        self.txtstinp = TxtStickInput(self.txt, True)
        self.verbose = verbose


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
