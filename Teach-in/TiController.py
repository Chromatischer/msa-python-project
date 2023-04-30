#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import select
import tty
from InputMethode import *
from TiModel import *
from TiView import *
from TiPosition import *
from TxtStickInput import *
from console_utils import *

inputMethode = InputMethode(["curses"])


class TiController():

    def getJoystickInput(self):
        if self.txtstinp.getButton("left"):
            self.tipos.append(TiPosition(self.tiModel.getCounterValue(1), self.tiModel.getCounterValue(2), self.tiModel.getCounterValue(3), self.tiModel.getCounterValue(4)))
            print("left button press! ", self.tipos[len(self.tipos)-1].get_str())
            self.txt.updateWait(0.7)

        if self.txtstinp.getButton("right"):
            self.tiModel.TestMotors.Reset.m1()
            self.tiModel.TestMotors.Reset.m2()
            self.tiModel.TestMotors.Reset.m3()
            self.tiModel.TestMotors.Reset.m4()
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
                if self.verbose: print("right, X -> ", -round(self.txtstinp.getPos("right", "X")))
                self.tiModel.MovementAgent.DirectControl.Safe.m4(-self.txtstinp.getPos("right", "X"))
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
        print(ConsoleUtils.Colors.blue, "number of total elements in buffer: " + str(len(self.tipos)), ConsoleUtils.Colors.reset)
        for tiPosition in self.tipos:
            i += 1
            if self.verbose:
                print(ConsoleUtils.Colors.yellow, "executing run for element: ", ConsoleUtils.Colors.magenta, i, ConsoleUtils.Colors.yellow, " in tipos with values: ", tiPosition.get_str(), ConsoleUtils.Colors.reset)
            for m in range(4):
                m = m + 1
                if not tiPosition.get(m) == 0:
                    if self.verbose:
                        print(ConsoleUtils.Colors.yellow, "element: ", ConsoleUtils.Colors.magenta, i, ConsoleUtils.Colors.yellow, " motor: ", ConsoleUtils.Colors.magenta, m, ConsoleUtils.Colors.yellow, " current value: ", ConsoleUtils.Colors.magenta, self.tiModel.getCounterValue(m), ConsoleUtils.Colors.yellow, " target: ", ConsoleUtils.Colors.magenta, tiPosition.get(m), ConsoleUtils.Colors.reset)

                    if self.tiModel.getCounterValue(m) < tiPosition.get(m):
                        while self.tiModel.getCounterValue(m) < tiPosition.get(m):
                            # print("current value: ", self.tiModel.getCounterValue(m), " smaller target: ", tiPosition.get(m), " Direct-control set to 1")
                            #I have no clue what I am doing, nor have I gotten any Idea weather or not it will work!
                            to_exec: str = "self.tiModel.MovementAgent.DirectControl.Safe.m" + str(m) + "(1)"
                            exec(to_exec)
                    elif self.tiModel.getCounterValue(m) > tiPosition.get(m):
                        while self.tiModel.getCounterValue(m) > tiPosition.get(m):
                            # print("current value: ", self.tiModel.getCounterValue(m), " larger target: ", tiPosition.get(m), " Direct-control set to -1")
                            #I have no clue what I am doing, nor have I gotten any Idea weather or not it will work!
                            to_exec: str = "self.tiModel.MovementAgent.DirectControl.Safe.m" + str(m) + "(-1)"
                            exec(to_exec)

                    to_exec: str = "self.tiModel.MovementAgent.DirectControl.Safe.m" + str(m) + "(0)"
                    exec(to_exec)

                    if self.verbose:
                        print(ConsoleUtils.Colors.green, "current value after run: ", self.tiModel.getCounterValue(m), " target was: ", tiPosition.get(m), ConsoleUtils.Colors.reset)

    def getCursesInput(self):
        print(self.tiModel.getCounterValue(1), " ", self.tiModel.getCounterValue(2), " ", self.tiModel.getCounterValue(3), " ", self.tiModel.getCounterValue(4))
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)
            print("c = ", c)

            if c == 'a':
                if self.verbose: print("rotate left: ", self.rotate)
                if self.rotate == -1:
                    self.rotate = 0
                elif self.rotate == 0:
                    self.rotate = -1
            if c == 'd':
                if self.verbose: print("rotate right: ", self.rotate)
                if self.rotate == 1:
                    self.rotate = 0
                elif self.rotate == 0:
                    self.rotate = 1
            if c == 'w':
                if self.verbose:
                    print("move fwd: ", self.move_x)
                if self.move_x == -1:
                    self.move_x = 0
                elif self.move_x == 0:
                    self.move_x = -1
            if c == 's':
                if self.verbose: print("move bwd: ", self.move_x)
                if self.move_x == 1:
                    self.move_x = 0
                elif self.move_x == 0:
                    self.move_x = 1
            if c == 'r':
                if self.verbose:
                    print("move up: ", self.move_y)
                if self.move_y == -1:
                    self.move_y = 0
                elif self.move_y == 0:
                    self.move_y = -1
            if c == 'f':
                if self.verbose: print("move down: ", self.move_y)
                if self.move_y == 1:
                    self.move_y = 0
                elif self.move_y == 0:
                    self.move_y = 1
            if c == 'q':
                if self.verbose:
                    print("claw open: ", self.claw)
                if self.claw == -1:
                    self.claw = 0
                elif self.claw == 0:
                    self.claw = -1
            if c == 'e':
                if self.verbose: print("claw close: ", self.claw)
                if self.claw == 1:
                    self.claw = 0
                elif self.claw == 0:
                    self.claw = 1
            if c == ' ':
                self.tipos.append(TiPosition(self.tiModel.getCounterValue(1), self.tiModel.getCounterValue(2), self.tiModel.getCounterValue(3), self.tiModel.getCounterValue(4)))
                print("left button press! ", self.tipos[len(self.tipos)-1].get_str())
                self.txt.updateWait(0.7)
            if c == '\x0a':
                self.tiModel.TestMotors.Reset.m1()
                self.tiModel.TestMotors.Reset.m2()
                self.tiModel.TestMotors.Reset.m3()
                self.tiModel.TestMotors.Reset.m4()
                inputMethode.setInputMethode("file")
            if c == '\x1b':
                self.txt.stopOnline()
                exit(0)
        self.tiModel.MovementAgent.DirectControl.Safe.m4(self.rotate)
        self.tiModel.MovementAgent.DirectControl.Safe.m1(self.move_x)
        self.tiModel.MovementAgent.DirectControl.Safe.m2(self.move_y)
        self.tiModel.MovementAgent.DirectControl.Safe.m3(self.claw)

    def __init__(self, value_txt: ftrobopy, viewer: TiView, verbose=False):
        super().__init__()

        self.txt = value_txt
        self.viewer = viewer

        self.tiModel = TiModel(self.txt, v=False)
        self.txtstinp = TxtStickInput(self.txt, True)
        self.verbose = verbose
        self.tipos = list()

        self.rotate = 0
        self.move_x = 0
        self.move_y = 0
        self.claw = 0

        self.tipos.append(TiPosition(-100, -5, 1, 200))
        self.tipos.append(TiPosition(-200, -10, 0, 400))
        self.tipos.append(TiPosition(-50, 0, -1, -200))
        self.tipos.append(TiPosition(0, 0, 0, 200))
        self.tipos.append(TiPosition(0, 0, 0, 0))

    def run(self):
        # self.inputMethode: InputMethode 

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

        tty.setcbreak(sys.stdin.fileno())
        while True:
            if inputMethode.getInputMethode() == "joystick":
                self.getJoystickInput()
            elif inputMethode.getInputMethode() == "file":
                self.getFileInput()
            elif inputMethode.getInputMethode() == "curses":
                self.getCursesInput()
