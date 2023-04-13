#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ftrobopy
from datetime import datetime
from TouchStyle import *


def flush_write_buffer():
    global write_buffer_other
    global write_buffer_data
    global txt
    global textfield_other
    global textfield_data

    if textfield_other.text() != write_buffer_other:
        textfield_other.setText(write_buffer_other)


txt: ftrobopy = None
write_buffer_other: str
write_buffer_data: str

textfield_other: QLabel
textfield_data: QLabel

m1 = None
m2 = None
m2_counter: int = 0
i5 = None
m3 = None
m4 = None


class FtcGuiApplication(TouchApplication):
    ftc_gui_window: TouchWindow

    def __init__(self, args):

        global txt
        global write_buffer_data
        global write_buffer_other
        global textfield_other
        global textfield_data
        global m1
        global m2
        global m3
        global m4

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
            print("---------------------------------------------------------------------------------------------------")

            textfield_other = QLabel("empty")
            textfield_other.setAlignment(Qt.AlignCenter)
            textfield_other.setWordWrap(True)
            ftc_gui_window.setCentralWidget(textfield_other)

            textfield_data = QLabel("data")
            textfield_data.setAlignment(Qt.AlignTop)

            self.update_text = QTimer(self)  # create a timer
            self.update_text.timeout.connect(flush_write_buffer)  # connect timer to on_timer slot
            self.update_text.start(1000)  # fire timer every 1000ms or 1Hz

            print("initializing motor objects: 0%")
            m1 = txt.motor(1)
            print("initializing motor objects: 25%")
            m2 = txt.motor(2)
            print("initializing motor objects: 50%")
            m3 = txt.motor(3)
            print("initializing motor objects: 75%")
            m4 = txt.motor(4)
            print("initializing motor objects: 100%")

            create_thread_using_runnable()

        ftc_gui_window.show()
        self.exec()


class Runnable(QRunnable):
    def run(self):
        print("running 100%")

        global txt
        global write_buffer_other
        global m1
        global m2
        global m3
        global m4
        global m2_counter

        if txt:
            m2.setSpeed(300)
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if txt:
                motpos1 = m2_counter
                write_buffer_other = str(motpos1)

                if m2.getCurrentDistance() != 0:
                    print(m2.getCurrentDistance())
                    # m2.stop()

                    # txt.motor(1).setDistance(100)
            # print(FtcGuiApplication.other)


class RunnableUpdateM2Distance(QRunnable):
    def run(self):
        global txt
        global write_buffer_other
        global m1
        global m2
        global m3
        global m4
        global i5
        global m2_counter

        if txt:
            i5 = txt.resistor(5)
            while True:
                if i5.value() > 7390:
                    m2_counter += 1
                    print("1")
                    while not i5.value() < 7390:
                        pass
                    print("0")


def create_thread_using_runnable():
    print("creating thread", end="\r")
    # I have no fucking idea, why this throws errors like crazy, but it does and I don't give a f
    # app = QCoreApplication([])
    print("app set up! 25%", end="\r")
    runnable = Runnable()
    runnable_update = RunnableUpdateM2Distance()
    print("runnable obj created 50%", end="\r")
    QThreadPool.globalInstance().start(runnable)
    QThreadPool.globalInstance().start(runnable_update)
    print("running runnable obj 75%", end="\r")
    # sys.exit(app.exec_())


if __name__ == "__main__":
    print("starting program!")
    application = FtcGuiApplication(sys.argv)
