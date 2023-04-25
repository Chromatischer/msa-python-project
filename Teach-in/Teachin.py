#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ftrobopy import *
from TouchStyle import *
from TiView import *
from TiController import *
from TiModel import *
from SimpleTxtConnector import *


class SetupThreads:
    @staticmethod
    def start_model_control():
        global txt

        print("creating thread", end="\r")
        # I have no fucking idea, why this throws errors like crazy, but it does and I don't give a f
        # app = QCoreApplication([])
        print("app set up! 25%", end="\r")
        ti_control = TiController(txt)
        print("runnable obj created 50%", end="\r")
        QThreadPool.globalInstance().start(ti_control)
        print("running runnable obj 75%", end="\r")
        # sys.exit(app.exec_())

    @staticmethod
    def update_ti_view():
        TiView.update()


class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        global txt
        # txt: ftrobopy

        print("initializing FtcGuiApplication")
        TouchApplication.__init__(self, args)

        ftc_gui_window = TouchWindow("testWindow")

        # region: establish connection

        try:
            print("trying to connect to localhost")
            txt = ftrobopy.ftrobopy('localhost', 65000, False, True)

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
        # endregion

        else:
            print("connection established with device: ", str(txt.getDevicename()), " at port: ", str(txt.getPort()),
                  " running version: ", str(txt.getVersionNumber()))
            print("---------------------------------------------------------------------------------------------------")

            textfield_other = QLabel("empty")
            textfield_other.setAlignment(Qt.AlignCenter)
            textfield_other.setWordWrap(True)
            ftc_gui_window.setCentralWidget(textfield_other)

            self.update_text = QTimer(self)  # create a timer
            self.update_text.timeout.connect(SetupThreads.update_ti_view())  # connect timer to TiView update methode
            self.update_text.start(1000)  # fire timer every 1000ms or 1Hz

            SetupThreads.start_model_control()

        ftc_gui_window.show()
        self.exec()


if __name__ == "__main__":
    print("starting program!")
    stxtc = SimpleTxtConnector()
    global txt
    txt = stxtc.txt
    SetupThreads.start_model_control()

    # application = FtcGuiApplication(sys.argv)
