#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from TouchStyle import *

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)
        mtext = []
        mvalue = []
        grid = QGridLayout()

        for i in range(5):
            mtext.append(QLabel())
            if i == 4:
                mtext[i].setText('GRAB=')
            else:
                mtext[i].setText('M'+str(i)+'=')
            mtext[i].setAlignment(Qt.AlignLeft)
            mvalue.append(QLabel())
            mvalue[i].setText('0')
            mvalue[i].setAlignment(Qt.AlignRight)

            grid.addWidget(mtext[i], i, 1)
            grid.addWidget(mvalue[i], i, 2)

        status = QLabel()
        status.setText('Testing...')
        status.setAlignment(Qt.AlignCenter)

        grid.addWidget(status, 5, 1, 1, 2)

        w = TouchWindow("Grid+")
        w.centralWidget.setLayout(grid)
        w.show()
        self.exec_()

if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
