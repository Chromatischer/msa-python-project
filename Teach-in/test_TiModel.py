from TiModel import *
from SimpleTxtConnector import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    ftxt = stxtc.txt
    timodel = TiModel(ftxt)
    last = 0

    timodel.TestMotors.TestReset.m1()
    print(timodel.getCounterValue(1))
    while True:
        if timodel.getCounterValue(1) != last:
            print(timodel.getCounterValue(1))
            last = timodel.getCounterValue(1)
        timodel.MovementAgent.DirectControl.Safe.m1(-1)


    timodel.TestMotors.TestCounters.m2()
    timodel.TestMotors.TestCounters.m3()
    timodel.TestMotors.TestCounters.m4()

    timodel.TestMotors.TestReset.m1()
    timodel.TestMotors.TestReset.m2()
    timodel.TestMotors.TestReset.m3()
    timodel.TestMotors.TestReset.m4()
