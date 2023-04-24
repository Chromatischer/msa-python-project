from SimpleTxtConnector import *
from TxtStickInput import *
from TiMotor import *
from config import *
from TiModel import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    txt = stxtc.txt
    txtsi = TxtStickInput(txt, True)
    # tim = TiModel(txt)

    m1 = TiMotor(txt, 1, ConfigPy.min_speed_m1, ConfigPy.max_speed_m1, False)
    m4 = TiMotor(txt, 4, ConfigPy.min_speed_m4, ConfigPy.max_speed_m4, False)
    while True:
        while not m4.getTruePosition() > 100:
            m4.move(1)
        m4.move(0)
        while not m4.getTruePosition() < -100:
            m4.move(-1)
        m4.move(0)

    #while True:
    #    m1.move(-txtsi.getPos("left", "Y"))
    #    m4.move(-txtsi.getPos("right", "X"))
