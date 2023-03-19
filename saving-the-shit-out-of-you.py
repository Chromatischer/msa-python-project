import sys

import ftrobopy

from TouchStyle import *


class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        global txt
        global posM1, posM2, posM3, posM4

        TouchApplication.__init__(self, args)
        # Creates an empty MainWindow
        w = TouchWindow("Test")

        try:
            txt = ftrobopy.ftrobopy('ft-txt', 65000)  # connect to TXT's IO controller
        except:
            txt = None  # set TXT to "None" of connection failed

        if not txt:
            # display error if TXT could no be connected
            # error messages is centered and may span
            # over several lines
            err_msg = QLabel("could not connect to txt!")  # create the error message label
            err_msg.setWordWrap(True)  # allow it to wrap over several lines
            err_msg.setAlignment(Qt.AlignCenter)  # center it horizontally
            w.setCentralWidget(err_msg)  # attach it to the main output area
        else:
            # initialization went fine. So the main gui
            # is being drawn

            # configure all TXT outputs to normal mode
            M = [txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR]
            I = [(txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL),
                 (txt.C_SWITCH, txt.C_DIGITAL)]
            txt.setConfig(M, I)
            txt.updateConfig()

            self.timer = QTimer(self)  # create a timer
            self.timer.timeout.connect(self.on_timer)  # connect timer to on_timer slot
            self.timer.start(500)  # fire timer every 500ms (2 hz)

        w.show()
        self.exec_()


pos = []  # positionen aller Motoren werden hier gespeichert!


# do timed tasks
def on_timer():
    pass


class MovementAgent:
    @staticmethod
    def save_move(mot):
        if type(mot) != int:
            raise Exception("wrong input type! on saveMove call! Type: ", type(mot))
        else:
            if mot == 1:
                pass
                # move m1
            if mot == 2:
                pass
                # move m2
            if mot == 3:
                pass
                # move m3
            if mot == 4:
                pass
                # move m4
            # movement goes here!

    @staticmethod
    def get_mot_pos(mot):
        if type(mot) != int:
            raise Exception("wrong input type! on saveMove call! Type: ", type(mot))

        if (mot <= 4) & (mot >= 1):
            if mot == 1:
                return 2

            if mot == 2:
                return 3

            if mot == 3:
                return 6

            if mot == 4:
                return 1

            else:
                raise Exception("Index out of bound! Expected range: 1-4 received: ",  mot)


class DataHandler:
    @staticmethod
    def get_item(item):
        if type(item) != int:
            raise Exception("wrong input type! on saveMove call! Type: ", type(item))
        return pos[item]

    @staticmethod
    def set_item(key):
        if type(key) != int:
            raise Exception("wrong input type! on saveMove call! Type: ", type(key))

        value = MovementAgent.get_mot_pos(1), MovementAgent.get_mot_pos(2), MovementAgent.get_mot_pos(3), MovementAgent.get_mot_pos(4)  # this formats the correct values in the correct format!

        pos[key] = value


if __name__ == "__main__":
    print(DataHandler.get_item(1))
    DataHandler.set_item(1)
    print(DataHandler.get_item(1))

    # FtcGuiApplication(sys.argv)
