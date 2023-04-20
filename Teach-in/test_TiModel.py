from TiModel import *
from SimpleTxtConnector import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    ftxt = stxtc.txt
    timodel = TiModel(ftxt)
    #while True:
    #    print(ftxt.resistor(5).value())

    timodel.TestMotors.TestCounters.m1()
    timodel.TestMotors.TestCounters.m2()
    timodel.TestMotors.TestCounters.m3()
    timodel.TestMotors.TestCounters.m4()

    timodel.TestMotors.TestReset.m1()
    timodel.TestMotors.TestReset.m2()
    timodel.TestMotors.TestReset.m3()
    timodel.TestMotors.TestReset.m4()
