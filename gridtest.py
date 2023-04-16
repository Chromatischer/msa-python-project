#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from TouchStyle import *

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)

        mtext = []  # Text für Spalte links
        mvalue = [] # Werte in der Spalte rechts

        # Raster erstellen
        # https://www.tutorialspoint.com/pyqt/pyqt_qgridlayout_class.htm
        grid = QGridLayout()

        # 5 Zeilen: Motoren 0..4 und ein Greifer
        for i in range(5):
            # Labels erzeugen
            # https://www.tutorialspoint.com/pyqt/pyqt_qlabel_widget.htm
            mtext.append(QLabel())
            if i == 4:
                mtext[i].setText('GRAB=')
            else:
                mtext[i].setText('M'+str(i)+'=')
            mtext[i].setAlignment(Qt.AlignLeft)
            mvalue.append(QLabel())
            mvalue[i].setText('0')
            mvalue[i].setAlignment(Qt.AlignRight)
            # in Raster einfügen
            grid.addWidget(mtext[i], i, 1)
            grid.addWidget(mvalue[i], i, 2)

        # ganz unten kommt noch ein Statustext hin
        status = QLabel()
        status.setText('Testing...')
        status.setAlignment(Qt.AlignCenter)
        # Platzierung Zeile 5, Spalte 1 aber über 2 Spalten breit
        grid.addWidget(status, 5, 1, 1, 2)

        w = TouchWindow("Grid+")
        # Layout auf das erstellte Raster ändern
        # https://cfw.ftcommunity.de/ftcommunity-TXT/en/programming/python/tutorial-3.html
        w.centralWidget.setLayout(grid)
        w.show()
        self.exec_()

if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
