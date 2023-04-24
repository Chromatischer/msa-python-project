#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from ftrobopy import *
from config import *
from TiMotor import *


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
        m2 = TiMotor(txt, 2, ConfigPy.min_speed_m2, ConfigPy.max_speed_m2)
        m3 = TiMotor(txt, 3, ConfigPy.min_speed_m3, ConfigPy.max_speed_m3)
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

        class TestCounters:
            @staticmethod
            def m1():
                print("testing m1")
                global m1

                while m1.getTruePosition() == 0:
                    m1.move(-0.1)

                m1.move(0)
                print("testing of m1: DONE value: ", m1.getTruePosition())

            @staticmethod
            def m2():
                print("testing m2")
                global txt
                m2 = txt.motor(2)
                m2.setSpeed(ConfigPy.max_speed_m2)
                counter = 0

                while not counter > 0:
                    if txt.resistor(5).value() > 7390:
                        counter += 1
                        while not txt.resistor(5).value() < 7390:
                            pass

                m2.stop()
                print("testing counter m2: DONE value: ", counter)

            @staticmethod
            def m3():
                print("testing m3")
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
                print("testing m3: DONE")

            @staticmethod
            def m4():
                print("testing m4")
                global txt
                m4 = txt.motor(4)
                m4.setSpeed(ConfigPy.max_speed_m4)

                while m4.getCurrentDistance() == 0:
                    pass

                m4.stop()
                print("testing m4: DONE value: ", m4.getCurrentDistance())

        class TestReset:
            global txt

            @staticmethod
            def m1():
                print("resetting m1!")
                if not txt.input(3).state():
                    print("switch state false!")
                    while not txt.input(3).state():
                        m1.move(1)
                    print("switch state true: EXITING")
                elif txt.input(3).state():
                    print("switch state true!")
                    while txt.input(3).state():
                        m1.move(-1)
                    print("switch state false: RESETTING")
                    m1.move(0)
                    while not txt.input(3).state():
                        m1.move(1)
                    print("switch state true: EXITING")

                m1.move(0)
                m1.resetTruePosition()
                print("resetting m1: DONE!")

            @staticmethod
            def m2():
                print("resetting m2!")
                m2 = txt.motor(2)
                if not txt.input(1).state():
                    print("switch state false!")
                    m2.setSpeed(ConfigPy.max_speed_m2)
                    while not txt.input(1).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(1).state():
                    print("switch state true!")
                    m2.setSpeed(-ConfigPy.max_speed_m2)
                    while txt.input(1).state():
                        pass
                    print("switch state false: RESETTING")
                    m2.stop()
                    m2.setSpeed(ConfigPy.max_speed_m2)
                    while not txt.input(1).state():
                        pass
                    print("switch state true: EXITING")

                m2.stop()
                print("resetting m2: DONE")

            @staticmethod
            def m3():
                print("resetting m3!")
                m3 = txt.motor(3)
                if not txt.input(4).state():
                    print("switch state false!")
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    txt.updateWait(0.6)
                    print("waited 0.6s whilst moving")
                    if not txt.input(4).state():
                        print("switch state false! moving outwards")
                        m3.setSpeed(-ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(4).state():
                    print("switch state true!")
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    while txt.input(4).state():
                        pass
                    print("switch state false: RESETTING")
                    m3.stop()
                    m3.setSpeed(-ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        pass
                    print("switch state true: EXITING")

                m3.stop()
                print("resetting m3: DONE")

            @staticmethod
            def m4():
                print("resetting m4!")
                m4 = txt.motor(4)
                if not txt.input(2).state():
                    print("switch state false!")
                    if random.random() > 0.5:
                        m4.setSpeed(ConfigPy.max_speed_m4)
                    else:
                        m4.setSpeed(-ConfigPy.max_speed_m4)
                    while not txt.input(2).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(2).state():
                    print("switch state true!")
                    m4.setSpeed(ConfigPy.max_speed_m4)
                    while txt.input(2).state():
                        pass
                    print("switch state false: RESETTING")
                    m4.stop()
                    m4.setSpeed(-ConfigPy.max_speed_m4)
                    while not txt.input(2).state():
                        pass
                    print("switch state true: EXITING")

                m4.stop()
                print("resetting m4: DONE")
