import unittest
from position import *


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.pos = Position(0, 0, 0, 0)

    def test_zero_pos_m1(self):
        print("testing zero pos m1!")
        self.assertEqual(self.pos.__getattr__('m1'), 0)
        print("testing zero pos m1: DONE")

    def test_zero_pos_m2(self):
        print("testing zero pos m2!")
        self.assertEqual(self.pos.__getattr__('m2'), 0)
        print("testing zero pos m2: DONE")

    def test_zero_pos_m3(self):
        print("testing zero pos m3!")
        self.assertEqual(self.pos.__getattr__('m3'), 0)
        print("testing zero pos m3: DONE")

    def test_zero_pos_m4(self):
        print("testing zero pos m4!")
        self.assertEqual(self.pos.__getattr__('m4'), 0)
        print("testing zero pos m4: DONE")

    def test_rw_pos_m1(self):
        print("testing read-write for m1!")
        self.pos.__setattr__('m1', 64)
        self.assertEqual(self.pos.__getattr__('m1'), 64)
        self.pos.__setattr__('m1', -64)
        self.assertEqual(self.pos.__getattr__('m1'), -64)
        self.pos.__setattr__('m1', 0)
        self.assertEqual(self.pos.__getattr__('m1'), 0)
        print("testing read-write for m1: DONE")

    def test_rw_pos_m2(self):
        print("testing read-write for m2!")
        self.pos.__setattr__('m2', 64)
        self.assertEqual(self.pos.__getattr__('m2'), 64)
        self.pos.__setattr__('m2', -64)
        self.assertEqual(self.pos.__getattr__('m2'), -64)
        self.pos.__setattr__('m2', 0)
        self.assertEqual(self.pos.__getattr__('m2'), 0)
        print("testing read-write for m2: DONE")

    def test_rw_pos_m3(self):
        print("testing read-write for m3!")
        self.pos.__setattr__('m3', 64)
        self.assertEqual(self.pos.__getattr__('m3'), 64)
        self.pos.__setattr__('m3', -64)
        self.assertEqual(self.pos.__getattr__('m3'), -64)
        self.pos.__setattr__('m3', 0)
        self.assertEqual(self.pos.__getattr__('m3'), 0)
        print("testing read-write for m3: DONE")

    def test_rw_pos_m4(self):
        print("testing read-write for m4!")
        self.pos.__setattr__('m4', 64)
        self.assertEqual(self.pos.__getattr__('m4'), 64)
        self.pos.__setattr__('m4', -64)
        self.assertEqual(self.pos.__getattr__('m4'), -64)
        self.pos.__setattr__('m4', 0)
        self.assertEqual(self.pos.__getattr__('m4'), 0)
        print("testing read-write for m4: DONE")

    def test_resetattr_pos(self):
        print("testing reset for all!")
        self.pos.__resetattr__(100, 2, 16, 5)
        self.assertEqual(self.pos.__getattr__('m1'), 100)
        self.assertEqual(self.pos.__getattr__('m2'), 2)
        self.assertEqual(self.pos.__getattr__('m3'), 16)
        self.assertEqual(self.pos.__getattr__('m4'), 5)
        print("testing reset for all: DONE")


if __name__ == '__main__':
    unittest.main()
