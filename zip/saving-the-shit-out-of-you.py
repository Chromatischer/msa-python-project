import sys
from types import NoneType

import ftrobopy

from TouchStyle import *
from position import *


class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        global txt
        global posM1, posM2, posM3, posM4

        TouchApplication.__init__(self, args)
        # Creates an empty MainWindow
        w = TouchWindow("Test")

        try:
            txt = ftrobopy.ftrobopy('localhost', 65000)
        except TimeoutError:
            txt = None

        if not txt:
            try:
                txt = ftrobopy.ftrobopy('ft-txt', 65000)  # connect to TXT's IO controller
            except TimeoutError:
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

            self.timer_500ms = QTimer(self)  # create a timer
            self.timer_500ms.timeout.connect(self.on_timer_500_ms)  # connect timer to on_timer slot
            self.timer_500ms.start(500)  # fire timer every 500ms (2 hz)

        m1 = txt.motor(1)
        m1.setSpeed(100)
        txt.updateWait(200)
        m1.stop()

        w.show()
        self.exec_()


pos: list[Position] = []  # positionen aller Motoren werden hier gespeichert!


# do timed tasks
def on_timer_500_ms():
    DataHandler.create_item()


class MovementAgent:
    @staticmethod
    def save_move(mot: int):
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
    def get_mot_pos(mot: int):
        if 0 < mot < 5:  # lol stupid! simplification of: (mot >= 1) & (mot <= 4)
            if mot == 1:
                return int(txt.getMotorDistance(1))

            if mot == 2:
                return int(txt.getMotorDistance(2))

            if mot == 3:
                return int(txt.getMotorDistance(3))

            if mot == 4:
                return int(txt.getMotorDistance(4))
            else:
                raise Exception("Index out of bound! Expected range: 1-4 received: ", mot)

    @staticmethod
    def get_mot_pos(mot: int, debug: bool):
        if debug:
            if 0 < mot < 5:  # lol stupid! simplification of: (mot >= 1) & (mot <= 4)
                if mot == 1:
                    return 1

                if mot == 2:
                    return 5

                if mot == 3:
                    return 4

                if mot == 4:
                    return 7

            else:
                raise Exception("Index out of bound! Expected range: 1-4 received: ", mot)

        else:
            if 0 < mot < 5:  # lol stupid! simplification of: (mot >= 1) & (mot <= 4)
                return MovementAgent.get_mot_pos(mot)

            else:
                raise Exception("Index out of bound! Expected range: 1-4 received: ", mot)


class DataHandler:
    @staticmethod
    def get_item(item: int):
        if item <= len(pos):
            return pos[item - 1]
        else:
            pass

    @staticmethod
    def set_item_at_position(key: int, m1: int, m2: int, m3: int, m4: int):
        value = Position(m1, m2, m3, m4)
        pos[key] = value

    @staticmethod
    def create_item_with_value(m1: int, m2: int, m3: int, m4: int):
        value = Position(m1, m2, m3, m4)
        pos.append(value)

    @staticmethod
    def create_item():
        value = Position(MovementAgent.get_mot_pos(1), MovementAgent.get_mot_pos(2), MovementAgent.get_mot_pos(3),
                         MovementAgent.get_mot_pos(4))
        pos.append(value)

    @staticmethod
    def create_item_debug():
        value = Position(MovementAgent.get_mot_pos(1, True), MovementAgent.get_mot_pos(2, True),
                         MovementAgent.get_mot_pos(3, True),
                         MovementAgent.get_mot_pos(4, True))
        pos.append(value)

    @staticmethod
    def get_pos_as_str(location: int):

        if type(DataHandler.get_item(location)) is not NoneType:
            value: str = DataHandler.get_item(location).get_str() + ' at pos: [' + str(location) + ']'

        else:
            value = 'No position data at pos: [' + str(location) + ']'

        return value


if __name__ == "__main__":
    FtcGuiApplication(sys.argv)

    # FtcGuiApplication(sys.argv)
