#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ftrobopy import *
from config import *

txt


class TiModel:

    def __init__(self, main_txt: ftrobopy):
        global txt
        txt: ftrobopy = main_txt

    class MovementAgent:
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

    class TestMotors:
        global txt

        @staticmethod
        def m1():
            global txt
            m1 = txt.motor(1)
            m1.setSpeed(ConfigPy.speedM1)
            while m1.getCurrentDistance() == 0:
                pass
            print("testing of m1 counter working left at: ", m1.getCurrentDistance())

        @staticmethod
        def m2():
            global txt
            m2 = txt.motor(2)
            m2.setSpeed(ConfigPy.speedM2)

            if txt.resistor(5).value() > 7390:
                while not txt.resistor(5).value() < 7390:
                    pass

            print("testing of m2 counter working left after first cycle: ")

        @staticmethod
        def m3():
            pass

        @staticmethod
        def m4():
            global txt
            m4 = txt.motor(4)
            m4.setSpeed(ConfigPy.speedM4)
