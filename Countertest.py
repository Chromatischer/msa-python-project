#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy

txt=ftrobopy.ftrobopy('ft-txt', 65000)

m1 = txt.motor(1)

while m1.getCurrentDistance() == 0:
    m1.setSpeed(512)
print(m1.getCurrentDistance())
m1.stop()