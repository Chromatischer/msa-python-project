#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from datetime import datetime
from TouchStyle import *


class FtcGuiApplication(TouchApplication):
    ftc_gui_window: TouchWindow
    other: QLabel

    def __init__(self, args):
        print("initializing FtcGuiApplication")
        TouchApplication.__init__(self, args)

        ftc_gui_window = TouchWindow("testWindow")

        try:
            print("trying to connect to localhost")
            txt = ftrobopy.ftrobopy('localhost', 65000)

        except (TimeoutError, ConnectionRefusedError) as error:
            print("failed to connect to localhost: ", error)
            txt = None

        if not txt:
            try:
                print("trying to connect to W-lan host")
                txt = ftrobopy.ftrobopy('ft-txt', 65000)

            except (TimeoutError, ConnectionRefusedError) as error:
                print("failed to connect to W-lan host: ", error)
                txt = None

        if not txt:
            print("connection could not be established")
            err_msg = QLabel("Both connections refused, that is too sad!")
            err_msg.setWordWrap(True)
            err_msg.setAlignment(Qt.AlignCenter)
            ftc_gui_window.setCentralWidget(err_msg)
            exit(-1)
        else:
            print("connection established with device: ", str(txt.getDevicename()), " at port: ", str(txt.getPort()),
                  " running version: ", str(txt.getVersionNumber()))
            normal = QLabel("working hard fucking retard")
            normal.setWordWrap(True)
            normal.setAlignment(Qt.AlignCenter)
            ftc_gui_window.setCentralWidget(normal)
            FtcGuiApplication.other = QLabel("test")
            ftc_gui_window.setCentralWidget(FtcGuiApplication.other)
            current_time = datetime.now().strftime("%H:%M:%S")
            FtcGuiApplication.other.setText(current_time)

            create_thread_using_runnable()

        ftc_gui_window.show()
        self.exec()


class Runnable(QRunnable):
    def run(self):
        print("running")
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            # print(FtcGuiApplication.other)
            FtcGuiApplication.other.setText(current_time)


def create_thread_using_runnable():
    print("creating thread")
    # I have no fucking idea, why this throws errors like crazy, but it does and I dont give a f
    # app = QCoreApplication([])
    print("app set up!")
    runnable = Runnable()
    print("runnable obj created")
    QThreadPool.globalInstance().start(runnable)
    print("running runnable obj")
    # system.exit(app.exec_())


if __name__ == "__main__":
    print("main")
    application = FtcGuiApplication(sys.argv)
