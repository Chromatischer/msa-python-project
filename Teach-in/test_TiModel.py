import unittest

from TiModel import *
from unittest import *
from SimpleTxtConnector import *


class TestTiModel(unittest.TestCase):
    def setUp(self):
        self.stxtc = SimpleTxtConnector()
        self.tim = TiModel(self.stxtc.txt)

    def testM1(self):
        self.tim.TestMotors.m1()

    def testM2(self):
        self.tim.TestMotors.m2()

    def testM3(self):
        self.tim.TestMotors.m3()


if __name__ == "__main__":
    unittest.main()