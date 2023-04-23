from SimpleTxtConnector import *
from TxtStickInput import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    txt = stxtc.txt
    txtsi = TxtStickInput(txt, True)
    lastcountervalue: int = 0
    truecounter: int = 0
    m1 = txt.motor(1)
    while True:
        lastcountervalue = m1.getCurrentDistance()
        print(m1.getCurrentDistance(), " ", truecounter)
        if txtsi.getPos("left", "Y") > 0:
            m1.setSpeed(round(512 * txtsi.getPos("left", "Y")))
            truecounter += m1.getCurrentDistance() - lastcountervalue

        if txtsi.getPos("left", "Y") < 0:
            m1.setSpeed(round(512 * txtsi.getPos("left", "Y")))
            truecounter -= m1.getCurrentDistance() - lastcountervalue

        if txtsi.getPos("left", "Y") == 0:
            m1.stop()
