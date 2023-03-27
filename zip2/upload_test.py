#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from datetime import datetime
from TouchStyle import *

ftc_gui_window: TouchWindow
other: QLabel


class FtcGuiApplication(TouchApplication):

    def __init__(self, args):
        print("test!")
        TouchApplication.__init__(self, args)

        ftc_gui_window = TouchWindow("testWindow")

        try:
            txt = ftrobopy.ftrobopy("localhost", 65000)
        except TimeoutError:
            txt = None

        if not txt:
            err_msg = QLabel("Error blablabla")
            err_msg.setWordWrap(True)
            err_msg.setAlignment(Qt.AlignCenter)
            ftc_gui_window.setCentralWidget(err_msg)
        else:
            normal = QLabel("working hard fucking retard")
            normal.setWordWrap(True)
            normal.setAlignment(Qt.AlignCenter)
            ftc_gui_window.setCentralWidget(normal)
            other = QLabel("test")
            ftc_gui_window.setCentralWidget(other)
            current_time = datetime.now().strftime("%H:%M:%S")
            other.setText(current_time)
        ftc_gui_window.show()
        create_thread_using_runnable()
        self.exec()


class Runnable(QRunnable):
    def run(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        other.setText(current_time)


def create_thread_using_runnable():
    app = QCoreApplication([])
    runnable = Runnable()
    QThreadPool.globalInstance().start(runnable)
    sys.exit(app.exec())


if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
