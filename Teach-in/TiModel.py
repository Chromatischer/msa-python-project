#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from ftrobopy import *
from config import *
from TiMotor import *
from console_utils import *


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#      _____                    _____                    _____                   _______                   _____                    _____                    _____  #
#     /\    \                  /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \ #
#    /::\    \                /::\    \                /::\____\               /::::\    \               /::\    \                /::\    \                /::\____\#
#    \:::\    \               \:::\    \              /::::|   |              /::::::\    \             /::::\    \              /::::\    \              /:::/    /#
#     \:::\    \               \:::\    \            /:::::|   |             /::::::::\    \           /::::::\    \            /::::::\    \            /:::/    / #
#      \:::\    \               \:::\    \          /::::::|   |            /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /:::/    /  #
#       \:::\    \               \:::\    \        /:::/|::|   |           /:::/    \:::\    \       /:::/  \:::\    \        /:::/__\:::\    \        /:::/    /   #
#       /::::\    \              /::::\    \      /:::/ |::|   |          /:::/    / \:::\    \     /:::/    \:::\    \      /::::\   \:::\    \      /:::/    /    #
#      /::::::\    \    ____    /::::::\    \    /:::/  |::|___|______   /:::/____/   \:::\____\   /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/    /     #
#     /:::/\:::\    \  /\   \  /:::/\:::\    \  /:::/   |::::::::\    \ |:::|    |     |:::|    | /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/    /      #
#    /:::/  \:::\____\/::\   \/:::/  \:::\____\/:::/    |:::::::::\____\|:::|____|     |:::|    |/:::/____/     \:::|    |/:::/__\:::\   \:::\____\/:::/____/       #
#   /:::/    \::/    /\:::\  /:::/    \::/    /\::/    / ~~~~~/:::/    / \:::\    \   /:::/    / \:::\    \     /:::|____|\:::\   \:::\   \::/    /\:::\    \       #
#  /:::/    / \/____/  \:::\/:::/    / \/____/  \/____/      /:::/    /   \:::\    \ /:::/    /   \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\    \      #
# /:::/    /            \::::::/    /                       /:::/    /     \:::\    /:::/    /     \:::\    \ /:::/    /    \:::\   \:::\    \       \:::\    \     #
# /:::/    /              \::::/____/                       /:::/    /       \:::\__/:::/    /       \:::\    /:::/    /      \:::\   \:::\____\       \:::\    \    #
# \::/    /                \:::\    \                      /:::/    /         \::::::::/    /         \:::\  /:::/    /        \:::\   \::/    /        \:::\    \   #
# \/____/                  \:::\    \                    /:::/    /           \::::::/    /           \:::\/:::/    /          \:::\   \/____/          \:::\    \  #
#                           \:::\    \                  /:::/    /             \::::/    /             \::::::/    /            \:::\    \               \:::\    \ #
#                            \:::\____\                /:::/    /               \::/____/               \::::/    /              \:::\____\               \:::\____\#
#                             \::/    /                \::/    /                 ~~                      \::/____/                \::/    /                \::/    /#
#                              \/____/                  \/____/                                           ~~                       \/____/                  \/____/ #
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                           Logo by: https://de.rakko.tools/tools/68/                                                               #
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#            this is one of the core files of the MSA-Project! It is the part, wich will do the heavy lifting to control and record movements of the model          #
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#


class TiModel:

    def __init__(self, main_txt: ftrobopy, v: bool = False):
        global m1, m2, m3, m4, txt, verbose
        txt = main_txt
        verbose = v
        m1 = TiMotor(txt, 1, ConfigPy.min_speed_m1, ConfigPy.max_speed_m1)
        m4 = TiMotor(txt, 4, ConfigPy.min_speed_m4, ConfigPy.max_speed_m4)

    @staticmethod
    def getCounterValue(motnum: int):
        if motnum == 1:
            return m1.getTruePosition()
        elif motnum == 2:
            return m2.getTruePosition()
        elif motnum == 3:
            return m3.getTruePosition()
        elif motnum == 4:
            return m4.getTruePosition()
        else:
            raise ValueError("motnum must be 1-4!")

    class MovementAgent:
        class DirectControl:
            class Unsafe:
                @staticmethod
                def move_m1(p: float):
                    """
                    moves the motor m1 with the speed in the ConfigPy multiplied by the param p!
                    :param p: the multiplicator by wich the config Speed will be multiplied
                    """

                    if p > 1 or p < -1:
                        raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                    else:
                        txt.motor(1).setSpeed(round(512 * p))

                @staticmethod
                def move_m2(p: float):
                    """
                    moves the motor m2 with the speed in the ConfigPy multiplied by the param p!
                    :param p: the multiplicator by wich the config Speed will be multiplied
                    """

                    if p > 1 or p < -1:
                        raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                    else:
                        txt.motor(2).setSpeed(round(512 * p))

                @staticmethod
                def move_m3(p: float):
                    """
                    moves the motor m3 with the speed in the ConfigPy multiplied by the param p!
                    :param p: the multiplicator by wich the config Speed will be multiplied
                    """

                    if p > 1 or p < -1:
                        raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                    else:
                        txt.motor(3).setSpeed(round(512 * p))

                @staticmethod
                def move_m4(p: float):
                    """
                    moves the motor m4 with the speed in the ConfigPy multiplied by the param p!
                    :param p: the multiplicator by wich the config Speed will be multiplied
                    """

                    if p > 1 or p < -1:
                        raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                    else:
                        txt.motor(4).setSpeed(round(512 * p))

            class Safe:
                @staticmethod
                def m1(p: float):
                    if p > 0:
                        if not txt.input(3).state():
                            if verbose:
                                print("moving m1! speed: ", round(ConfigPy.max_speed_m1 * p))
                            m1.move(p)
                        else:
                            if verbose:
                                print("not moving m1 because: stop switch state: ", bool(txt.input(3).state()))
                            m1.move(0)
                    elif p < 0:
                        if not m1.getTruePosition() < -1200:
                            if verbose:
                                print("moving m1! speed: ", round(ConfigPy.max_speed_m1 * p))
                            m1.move(p)
                        else:
                            if verbose:
                                print("not moving m1 because: current counter value: ",
                                      txt.motor(1).getCurrentDistance())
                            m1.move(0)
                    else:
                        m1.move(0)
                        if verbose:
                            print("stopped motor because: p ==", p)

    class TestMotors:
        global txt

        class Counters:
            @staticmethod
            def m1():
                print(ConsoleUtils.Colors.blue, "testing m1", ConsoleUtils.Colors.reset)
                global m1

                while m1.getTruePosition() == 0:
                    m1.move(-0.1)

                m1.move(0)
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing of m1: DONE value: ", m1.getTruePosition(), ConsoleUtils.Colors.reset)

            @staticmethod
            def m2():
                print(ConsoleUtils.Colors.blue, "testing m2", ConsoleUtils.Colors.reset)
                global txt
                m2 = txt.motor(2)
                m2.setSpeed(ConfigPy.max_speed_m2)
                counter = 0

                while not counter > 0:
                    if txt.resistor(5).value() > 7390:
                        counter += 1
                        while not txt.resistor(5).value() < 7390:
                            txt.updateWait()

                m2.stop()
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing counter m2: DONE value: ", counter, ConsoleUtils.Colors.reset)

            @staticmethod
            def m3():
                print(ConsoleUtils.Colors.blue, "testing m3", ConsoleUtils.Colors.reset)
                global txt
                m3 = txt.motor(3)
                m3.setSpeed(-ConfigPy.max_speed_m3)

                if txt.input(4).state():
                    while not not txt.input(4).state():
                        pass
                else:
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        pass

                m3.stop()
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing m3: DONE", ConsoleUtils.Colors.reset)

            @staticmethod
            def m4():
                print(ConsoleUtils.Colors.blue, "testing m4", ConsoleUtils.Colors.reset)
                global txt
                m4 = txt.motor(4)
                m4.setSpeed(ConfigPy.max_speed_m4)

                while m4.getCurrentDistance() == 0:
                    pass

                m4.stop()
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing m4: DONE value: ", m4.getCurrentDistance(), ConsoleUtils.Colors.reset)

        class Reset:
            global txt

            @staticmethod
            def m1():
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.blue, "resetting m1!", ConsoleUtils.Colors.reset)
                if not txt.input(3).state():
                    print(ConsoleUtils.Colors.yellow, "switch state false!", ConsoleUtils.Colors.reset)
                    while not txt.input(3).state():
                        m1.move(1)
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)
                elif txt.input(3).state():
                    print(ConsoleUtils.Colors.yellow, "switch state true!", ConsoleUtils.Colors.reset)
                    while txt.input(3).state():
                        m1.move(-1)
                    print(ConsoleUtils.Colors.yellow, "switch state false: RESETTING", ConsoleUtils.Colors.reset)
                    m1.move(0)
                    while not txt.input(3).state():
                        m1.move(1)
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)

                m1.move(0)
                m1.resetTruePosition()
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m1: DONE!", ConsoleUtils.Colors.reset)

            @staticmethod
            def m2():
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.blue, "resetting m2!", ConsoleUtils.Colors.reset)
                m2 = txt.motor(2)
                if not txt.input(1).state():
                    print(ConsoleUtils.Colors.yellow, "switch state false!", ConsoleUtils.Colors.reset)
                    m2.setSpeed(ConfigPy.max_speed_m2)
                    while not txt.input(1).state():
                        pass
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)
                elif txt.input(1).state():
                    print(ConsoleUtils.Colors.yellow, "switch state true!", ConsoleUtils.Colors.reset)
                    m2.setSpeed(-ConfigPy.max_speed_m2)
                    while txt.input(1).state():
                        pass
                    print(ConsoleUtils.Colors.yellow, "switch state false: RESETTING", ConsoleUtils.Colors.reset)
                    m2.stop()
                    m2.setSpeed(ConfigPy.max_speed_m2)
                    while not txt.input(1).state():
                        pass
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)

                m2.stop()
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m2: DONE", ConsoleUtils.Colors.reset)

            @staticmethod
            def m3():
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.blue, "resetting m3!", ConsoleUtils.Colors.reset)
                m3 = txt.motor(3)
                if not txt.input(4).state():
                    print(ConsoleUtils.Colors.yellow, "switch state false!", ConsoleUtils.Colors.reset)
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    txt.updateWait(0.6)
                    print(ConsoleUtils.Colors.yellow, "waited 0.6s whilst moving", ConsoleUtils.Colors.reset)
                    if not txt.input(4).state():
                        print(ConsoleUtils.Colors.yellow, "switch state false! moving outwards", ConsoleUtils.Colors.reset)
                        m3.setSpeed(-ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        pass
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)
                elif txt.input(4).state():
                    print(ConsoleUtils.Colors.yellow, "switch state true!", ConsoleUtils.Colors.reset)
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    while txt.input(4).state():
                        pass
                    print(ConsoleUtils.Colors.yellow, "switch state false: RESETTING", ConsoleUtils.Colors.reset)
                    m3.stop()
                    m3.setSpeed(-ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        pass
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)

                m3.stop()
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m3: DONE", ConsoleUtils.Colors.reset)

            @staticmethod
            def m4():
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.blue, "resetting m4!", ConsoleUtils.Colors.reset)
                if not txt.input(2).state():
                    print(ConsoleUtils.Colors.yellow, "switch state false!", ConsoleUtils.Colors.reset)
                    while not txt.input(2).state():
                        m4.move(1)
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)
                elif txt.input(2).state():
                    print(ConsoleUtils.Colors.yellow, "switch state true!", ConsoleUtils.Colors.reset)
                    while txt.input(2).state():
                        m4.move(1)
                    print(ConsoleUtils.Colors.yellow, "switch state false: RESETTING", ConsoleUtils.Colors.reset)
                    m4.move(0)
                    while not txt.input(2).state():
                        m4.move(-1)
                    print(ConsoleUtils.Colors.green, "switch state true: EXITING", ConsoleUtils.Colors.reset)

                m4.move(0)
                m4.resetTruePosition()
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m4: DONE", ConsoleUtils.Colors.reset)
