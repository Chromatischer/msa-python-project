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
        global m1, m2, m3, m4, txt, verbose, _counter_m2, _counter_m3
        txt = main_txt
        verbose = v
        m1 = TiMotor(txt, 1, ConfigPy.min_speed_m1, ConfigPy.max_speed_m1, verbose=False)
        m2 = txt.motor(2)
        m3 = txt.motor(3)
        m4 = TiMotor(txt, 4, ConfigPy.min_speed_m4, ConfigPy.max_speed_m4, verbose=False)
        _counter_m2 = 0
        _counter_m3 = 0

    @staticmethod
    def getCounterValue(motnum: int):
        global m1, m2, m3, m4, txt, verbose, _counter_m2, counter_m3
        if motnum == 1:
            return m1.getTruePosition()
        elif motnum == 2:
            return _counter_m2
        elif motnum == 3:
            return _counter_m3
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
                            m1.resetTruePosition()
                            if verbose:
                                print("reset position value for m1: hard switch point reached!")
                    elif p < 0:
                        if not m1.getTruePosition() < -850:
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

                @staticmethod
                def m2(p: float):
                    global _counter_m2, m2, m3, _counter_m3
                    if p > 1 or p < -1:
                        raise ValueError("parameter value out of bound for range: -1 - 1")
                    else:
                        if p > 0:
                            if not txt.input(1).state():
                                if verbose:
                                    print("moving m2: ", p)
                                if round(ConfigPy.max_speed_m2 * p) < ConfigPy.min_speed_m2:
                                    m2.setSpeed(ConfigPy.min_speed_m2)
                                    if verbose:
                                        print("spd:", ConfigPy.min_speed_m2)
                                else:
                                    m2.setSpeed(round(ConfigPy.max_speed_m2 * p))
                                    if verbose:
                                        print("spd: ", round(ConfigPy.max_speed_m2 * p))

                                c_res5_noop = 0
                                reset_spd_m2 = False

                                #region while > 7390
                                while not txt.resistor(5).value() > 7390:
                                    txt.updateWait()
                                    c_res5_noop += 1
                                    if c_res5_noop > 30:
                                        print(ConsoleUtils.Colors.red, "waited for: ", c_res5_noop,
                                              " cycles without resistor value! setting speed to min value!")
                                        m2.setSpeed(-ConfigPy.min_speed_m2)
                                        print("spd:", -ConfigPy.min_speed_m2)
                                        reset_spd_m2 = True
                                #endregion

                                #region reset speed if needed!
                                if reset_spd_m2:
                                    if round(ConfigPy.max_speed_m2 * p) < ConfigPy.min_speed_m2:
                                        m2.setSpeed(ConfigPy.min_speed_m2)
                                        print("spd:", ConfigPy.min_speed_m2)
                                    else:
                                        m2.setSpeed(round(ConfigPy.max_speed_m2 * p))
                                        print("spd:", round(ConfigPy.max_speed_m2 * p))
                                #endregion

                                _counter_m2 += 1

                                if verbose:
                                    print(_counter_m2)

                                #region while < 7390
                                while not txt.resistor(5).value() < 7390:
                                    txt.updateWait()
                                #endregion
                            else:
                                m2.stop()
                                _counter_m2 = 0
                                if verbose:
                                    print("reset m2 counter for better accuracy at 0 pos")
                                if verbose:
                                    print("not moving m2 because: stop switch state: ", bool(txt.input(1).state()))
                        elif p < 0:
                            if not _counter_m2 < -70:
                                if verbose:
                                    print("moving m2: ", p)
                                if round(ConfigPy.max_speed_m2 * p) < ConfigPy.min_speed_m2:
                                    m2.setSpeed(-ConfigPy.min_speed_m2)
                                    if verbose:
                                        print("spd:", -ConfigPy.min_speed_m2)
                                else:
                                    m2.setSpeed(-round(ConfigPy.max_speed_m2 * p))
                                    if verbose:
                                        print("spd:", -round(ConfigPy.max_speed_m2 * p))

                                c_res5_noop = 0
                                reset_spd_m2 = False

                                #region while > 7390
                                while not txt.resistor(5).value() > 7390:
                                    txt.updateWait()
                                    c_res5_noop += 1
                                    if c_res5_noop > 30:
                                        print(ConsoleUtils.Colors.red, "waited for: ", c_res5_noop, " cycles without resistor value! setting speed to min value!")
                                        m2.setSpeed(-ConfigPy.min_speed_m2)
                                        if verbose:
                                            print("spd:", -ConfigPy.min_speed_m2)
                                        reset_spd_m2 = True
                                #endregion

                                #region reset speed if needed
                                if reset_spd_m2:
                                    if round(ConfigPy.max_speed_m2 * p) < ConfigPy.min_speed_m2:
                                        m2.setSpeed(-ConfigPy.min_speed_m2)
                                        if verbose:
                                            print("spd:", -ConfigPy.min_speed_m2)
                                    else:
                                        m2.setSpeed(round(ConfigPy.max_speed_m2 * p))
                                        if verbose:
                                            print("spd:", -round(ConfigPy.max_speed_m2 * p))
                                #endregion

                                _counter_m2 -= 1

                                if verbose:
                                    print(_counter_m2)

                                #region while < 7390
                                while not txt.resistor(5).value() < 7390:
                                    txt.updateWait()
                                #endregion
                            else:
                                if verbose:
                                    print("not moving m2 because: current counter value: ", _counter_m2)
                                m2.stop()
                        else:
                            m2.stop()
                            if verbose:
                                print("stopped motor because: p ==", p)

                @staticmethod
                def m3(p: float):
                    global m3, _counter_m3
                    if txt.input(4).state():
                        _counter_m3 = 0
                        if verbose:
                            print("reset counter m3: hard switch state reached!")
                    if p > 0:
                        if _counter_m3 == 0:
                            if verbose:
                                print("p > 0 counter == 0")
                            if ConfigPy.max_speed_m3 * p < ConfigPy.min_speed_m3:
                                m3.setSpeed(-ConfigPy.min_speed_m3)
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -ConfigPy.min_speed_m3)
                            else:
                                m3.setSpeed(-round(ConfigPy.max_speed_m3 * p))
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -round(ConfigPy.max_speed_m3 * p))
                            while bool(txt.input(4).state()):
                                txt.updateWait()
                            m3.stop()
                            _counter_m3 = 1
                            if verbose:
                                print(_counter_m3)

                        elif _counter_m3 == -1:
                            if verbose:
                                print("p > 0 counter == -1")
                            if ConfigPy.max_speed_m3 * p < ConfigPy.min_speed_m3:
                                m3.setSpeed(-ConfigPy.min_speed_m3)
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -ConfigPy.min_speed_m3)
                            else:
                                m3.setSpeed(-round(ConfigPy.max_speed_m3 * p))
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -round(ConfigPy.max_speed_m3 * p))
                            while not txt.input(4).state():
                                txt.updateWait()
                            m3.stop()
                            _counter_m3 = 0
                            if verbose:
                                print(_counter_m3)

                    elif p < 0:
                        if _counter_m3 == 1:
                            if verbose:
                                print("p < 0 counter == 1")
                                print(txt.input(4).state())
                            if ConfigPy.max_speed_m3 * -p < ConfigPy.min_speed_m3:
                                m3.setSpeed(ConfigPy.min_speed_m3)
                                if verbose:
                                    print("moving m3: ", p, " spd: ", ConfigPy.min_speed_m3)
                            else:
                                m3.setSpeed(-round(ConfigPy.max_speed_m3 * p))
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -round(ConfigPy.max_speed_m3 * p))
                            while not bool(txt.input(4).state()):
                                txt.updateWait()
                            m3.stop()
                            _counter_m3 = 0
                            if verbose:
                                print(_counter_m3)

                        elif _counter_m3 == 0:
                            if verbose:
                                print("p < 0 counter == 0")
                            if ConfigPy.max_speed_m3 * -p < ConfigPy.min_speed_m3:
                                m3.setSpeed(ConfigPy.min_speed_m3)
                                if verbose:
                                    print("moving m3: ", p, " spd: ", ConfigPy.min_speed_m3)
                            else:
                                m3.setSpeed(-round(ConfigPy.max_speed_m3 * p))
                                if verbose:
                                    print("moving m3: ", p, " spd: ", -round(ConfigPy.max_speed_m3 * p))
                            while txt.input(4).state():
                                txt.updateWait()
                            m3.stop()
                            _counter_m3 = -1
                            if verbose:
                                print(_counter_m3)
                    else:
                        m3.stop()
                        if verbose:
                            print("stopped motor because: p == ", p)

                @staticmethod
                def m4(p: float):
                    if txt.input(2).state():
                        m4.resetTruePosition()
                        if verbose:
                            print("reset m4 position variable: switch point reached!")
                    if p > 0:
                        if not m4.getTruePosition() > 800:
                            if verbose:
                                print("moving m4! speed: ", round(ConfigPy.max_speed_m4 * p))
                            m4.move(p)
                        else:
                            if verbose:
                                print("not moving m4 because: hard limit was reached!")
                            m4.move(0)
                    elif p < 0:
                        if not m4.getTruePosition() < -800:
                            if verbose:
                                print("moving m4! speed: ", round(ConfigPy.max_speed_m4 * p))
                            m4.move(p)

                        else:
                            if verbose:
                                print("not moving m4 because: hard limit was reached!")
                            m4.move(0)
                    else:
                        m4.move(0)
                        if verbose:
                            print("stopped motor because: p ==", p)

    class TestMotors:
        global txt, _counter_m2

        class Counters:
            @staticmethod
            def m1():
                print(ConsoleUtils.Colors.blue, "testing m1", ConsoleUtils.Colors.reset)
                global m1

                while m1.getTruePosition() == 0:
                    m1.move(-0.1)

                m1.move(0)
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing of m1: DONE value: ",
                      m1.getTruePosition(), ConsoleUtils.Colors.reset)

            @staticmethod
            def m2():
                print(ConsoleUtils.Colors.blue, "testing m2", ConsoleUtils.Colors.reset)
                global txt
                m2 = txt.motor(2)
                m2.setSpeed(-ConfigPy.max_speed_m2)
                counter = 0

                while not counter > 2:
                    if txt.resistor(5).value() > 7390:
                        counter += 1
                        while not txt.resistor(5).value() < 7390:
                            txt.updateWait()

                m2.stop()
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing counter m2: DONE value: ", counter,
                      ConsoleUtils.Colors.reset)

            @staticmethod
            def m3():
                print(ConsoleUtils.Colors.blue, "testing m3", ConsoleUtils.Colors.reset)
                global txt
                m3 = txt.motor(3)
                m3.setSpeed(-ConfigPy.max_speed_m3)

                if txt.input(4).state():
                    while not not txt.input(4).state():
                        txt.updateWait(0.4)
                        if not txt.input(4).state():
                            m3.setSpeed(ConfigPy.max_speed_m3)
                else:
                    m3.setSpeed(ConfigPy.max_speed_m3)
                    while not txt.input(4).state():
                        txt.updateWait(0.4)
                        if not txt.input(4).state():
                            m3.setSpeed(-ConfigPy.max_speed_m3)

                m3.stop()
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing m3: DONE",
                      ConsoleUtils.Colors.reset)

            @staticmethod
            def m4():
                print(ConsoleUtils.Colors.blue, "testing m4", ConsoleUtils.Colors.reset)
                global txt

                while m4.getTruePosition() == 0:
                    m4.move(1)

                m4.move(0)
                print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "testing m4: DONE value: ",
                      m4.getTruePosition(), ConsoleUtils.Colors.reset)

        class Reset:
            global txt, _counter_m2

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
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m1: DONE!",
                      ConsoleUtils.Colors.reset)

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
                _counter_m2 = 0
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m2: DONE",
                      ConsoleUtils.Colors.reset)

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
                        print(ConsoleUtils.Colors.yellow, "switch state false! moving outwards",
                              ConsoleUtils.Colors.reset)
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
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m3: DONE",
                      ConsoleUtils.Colors.reset)

            @staticmethod
            def m4():
                m4.resetTruePosition()
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.blue, "resetting m4!", ConsoleUtils.Colors.reset)
                if not txt.input(2).state():
                    print(ConsoleUtils.Colors.yellow, "switch state false!", ConsoleUtils.Colors.reset)
                    while not txt.input(2).state() and m4.getTruePosition() < 800:
                        m4.move(1)
                    m4.move(0)
                    while not txt.input(2).state() and m4.getTruePosition() > -800:
                        m4.move(-1)
                    m4.move(0)
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
                print(ConsoleUtils.Stiles.bold, ConsoleUtils.Colors.green, "resetting m4: DONE",
                      ConsoleUtils.Colors.reset)
