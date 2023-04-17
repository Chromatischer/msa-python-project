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
        for i in range(6):
            # Labels erzeugen
            # https://www.tutorialspoint.com/pyqt/pyqt_qlabel_widget.htm
            mtext.append(QLabel())
            if i == 4:
                mtext[i].setText('grab:')
            elif i == 5:
                mtext[i].setText('steps:')
            else:
                mtext[i].setText('M'+str(i)+'=')
            mtext[i].setAlignment(Qt.AlignLeft)
            mvalue.append(QLabel())
            mvalue[i].setText('0')
            mvalue[i].setAlignment(Qt.AlignLeft)
            # in Raster einfügen
            if (i % 2) == 0:
                # ungerade links
                grid.addWidget(mtext[i], int(i / 2), 1)
                grid.addWidget(mvalue[i], int(i / 2), 2)
            else:
                # gerade rechts
                grid.addWidget(mtext[i], int(i / 2), 3)
                grid.addWidget(mvalue[i], int(i / 2), 4)

        # ganz unten kommt noch ein Statustext hin
        status = QLabel()
        status.setText('Testing...')
        status.setAlignment(Qt.AlignCenter)
        # Platzierung Zeile 5, Spalte 1 aber über 4 Spalten breit
        grid.addWidget(status, 6, 1, 1, 4)

        # Knopf zum Beenden
        endbutton = QPushButton("Record Stop")
        # auch über die ganze Breite
        grid.addWidget(endbutton, 7, 1, 1, 4)

        w = TouchWindow("Teach In")
        # Layout auf das erstellte Raster ändern
        # https://cfw.ftcommunity.de/ftcommunity-TXT/en/programming/python/tutorial-3.html
        w.centralWidget.setLayout(grid)
        w.show()
        self.exec_()

if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
