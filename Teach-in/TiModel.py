#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from ftrobopy import *
from config import *

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

txt = None


class TiModel:

    def __init__(self, main_txt: ftrobopy):
        global txt
        txt = main_txt

    class MovementAgent:
        global txt

        @staticmethod
        def move_x():
            pass

        @staticmethod
        def move_y():
            pass

        @staticmethod
        def move_grab():
            pass

        @staticmethod
        def move_rotate():
            pass

        class DirectControl:
            """
            allows for direct controll of the motors without having any safety installed! Careful it may be harmful!

            **DO NOT USE** (except for debugging)

            **USE: MovementAgent.move_<xyz>()**
            """

            @staticmethod
            def move_m1(p: float):
                """
                moves the motor m1 with the speed in the ConfigPy multiplied by the param p!
                :param p: the multiplicator by wich the config Speed will be multiplied
                """

                if p > 1 or p < -1:
                    raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                else:
                    txt.motor(1).setSpeed(round(ConfigPy.speedM1 * p))

            @staticmethod
            def move_m2(p: float):
                """
                moves the motor m2 with the speed in the ConfigPy multiplied by the param p!
                :param p: the multiplicator by wich the config Speed will be multiplied
                """

                if p > 1 or p < -1:
                    raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                else:
                    txt.motor(2).setSpeed(round(ConfigPy.speedM2 * p))

            @staticmethod
            def move_m3(p: float):
                """
                moves the motor m3 with the speed in the ConfigPy multiplied by the param p!
                :param p: the multiplicator by wich the config Speed will be multiplied
                """

                if p > 1 or p < -1:
                    raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                else:
                    txt.motor(3).setSpeed(round(ConfigPy.speedM3 * p))

            @staticmethod
            def move_m4(p: float):
                """
                moves the motor m4 with the speed in the ConfigPy multiplied by the param p!
                :param p: the multiplicator by wich the config Speed will be multiplied
                """

                if p > 1 or p < -1:
                    raise ValueError("input param p is out of bounds for value range -1.0 - 1.0")
                else:
                    txt.motor(4).setSpeed(round(ConfigPy.speedM4 * p))

    class TestMotors:
        global txt

        class TestCounters:
            @staticmethod
            def m2():
                print("testing m2")
                global txt
                m2 = txt.motor(2)
                m2.setSpeed(ConfigPy.speedM2)
                counter = 0

                while not counter > 0:
                    if txt.resistor(5).value() > 7390:
                        counter += 1
                        while not txt.resistor(5).value() < 7390:
                            pass

                m2.stop()
                print("testing counter m2: DONE value: ", counter)

            @staticmethod
            def m1():
                print("testing m1")
                global txt
                m1 = txt.motor(1)
                m1.setSpeed(ConfigPy.speedM1)

                while m1.getCurrentDistance() == 0:
                    pass

                m1.stop()
                print("testing of m1: DONE value: ", m1.getCurrentDistance())

            @staticmethod
            def m3():
                print("testing m3")
                global txt
                m3 = txt.motor(3)
                m3.setSpeed(-ConfigPy.speedM3)

                if txt.input(4).state():
                    while not not txt.input(4).state():
                        pass
                else:
                    m3.setSpeed(ConfigPy.speedM3)
                    while not txt.input(4).state():
                        pass

                m3.stop()
                print("testing m3: DONE")

            @staticmethod
            def m4():
                print("testing m4")
                global txt
                m4 = txt.motor(4)
                m4.setSpeed(ConfigPy.speedM4)

                while m4.getCurrentDistance() == 0:
                    pass

                m4.stop()
                print("testing m4: DONE value: ", m4.getCurrentDistance())

        class TestReset:
            global txt

            @staticmethod
            def m1():
                print("resetting m1!")
                m1 = txt.motor(1)
                if not txt.input(3).state():
                    print("switch state false!")
                    m1.setSpeed(ConfigPy.speedM1)
                    while not txt.input(3).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(3).state():
                    print("switch state true!")
                    m1.setSpeed(-ConfigPy.speedM1)
                    while txt.input(3).state():
                        pass
                    print("switch state false: RESETTING")
                    m1.stop()
                    m1.setSpeed(ConfigPy.speedM1)
                    while not txt.input(3).state():
                        pass
                    print("switch state true: EXITING")

                m1.stop()
                print("resetting m1: DONE!")

            @staticmethod
            def m2():
                print("resetting m2!")
                m2 = txt.motor(2)
                if not txt.input(1).state():
                    print("switch state false!")
                    m2.setSpeed(ConfigPy.speedM2)
                    while not txt.input(1).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(1).state():
                    print("switch state true!")
                    m2.setSpeed(-ConfigPy.speedM2)
                    while txt.input(1).state():
                        pass
                    print("switch state false: RESETTING")
                    m2.stop()
                    m2.setSpeed(ConfigPy.speedM2)
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
                    m3.setSpeed(ConfigPy.speedM3)
                    txt.updateWait(0.6)
                    print("waited 0.6s whilst moving")
                    if not txt.input(4).state():
                        print("switch state false! moving outwards")
                        m3.setSpeed(-ConfigPy.speedM3)
                    while not txt.input(4).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(4).state():
                    print("switch state true!")
                    m3.setSpeed(ConfigPy.speedM3)
                    while txt.input(4).state():
                        pass
                    print("switch state false: RESETTING")
                    m3.stop()
                    m3.setSpeed(-ConfigPy.speedM3)
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
                        m4.setSpeed(ConfigPy.speedM4)
                    else:
                        m4.setSpeed(-ConfigPy.speedM4)
                    while not txt.input(2).state():
                        pass
                    print("switch state true: EXITING")
                elif txt.input(2).state():
                    print("switch state true!")
                    m4.setSpeed(ConfigPy.speedM4)
                    while txt.input(2).state():
                        pass
                    print("switch state false: RESETTING")
                    m4.stop()
                    m4.setSpeed(-ConfigPy.speedM4)
                    while not txt.input(2).state():
                        pass
                    print("switch state true: EXITING")

                m4.stop()
                print("resetting m4: DONE")
