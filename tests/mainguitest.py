#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from TouchStyle import *

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)

        resetB = QPushButton("Reset Robot")
        selfTestB = QPushButton("Selftest Robot")
        teachInSessionB = QPushButton("Start Teach In")
        loadSessionB = QPushButton("Load Session")
        loadSessionB.clicked.connect(self.on_loadSessionB_clicked)
        deleteSessionB = QPushButton("Delete Session")

        vbox = QVBoxLayout()
        vbox.addWidget(resetB)
        vbox.addWidget(selfTestB)
        vbox.addWidget(teachInSessionB)
        vbox.addWidget(loadSessionB)
        vbox.addWidget(deleteSessionB)

        w = TouchWindow("Teach In")
        # Layout auf das erstellte Raster ändern
        # https://cfw.ftcommunity.de/ftcommunity-TXT/en/programming/python/tutorial-3.html
        w.centralWidget.setLayout(vbox)
        w.show()
        self.exec_()

    def on_loadSessionB_clicked(self):
        # loadfile = QFileDialog.getOpenFileName(self, 'Load Session', '.', "Sesions (*.ses)")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("We have to select files.")
        msg.setWindowTitle("Load Session")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec()

if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
