from TiModel import *
from SimpleTxtConnector import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    ftxt = stxtc.txt
    timodel = TiModel(ftxt, True)
    last = 0

    print("\n")
    print(ConsoleUtils.Colors.red, ConsoleUtils.Stiles.bold, "TESTING COUNTERS FOR ALL MOTORS!", ConsoleUtils.Colors.reset)
    timodel.TestMotors.Counters.m1()
    timodel.TestMotors.Counters.m2()
    timodel.TestMotors.Counters.m3()
    timodel.TestMotors.Counters.m4()
    print("\n")
    print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "ALL MOTOR COUNTERS WORKING!", ConsoleUtils.Colors.reset)

    print("\n")
    print(ConsoleUtils.Colors.red, ConsoleUtils.Stiles.bold, "RESETTING ALL MOTORS!", ConsoleUtils.Colors.reset)
    timodel.TestMotors.Reset.m1()
    timodel.TestMotors.Reset.m2()
    timodel.TestMotors.Reset.m3()
    timodel.TestMotors.Reset.m4()
    print("\n")
    print(ConsoleUtils.Colors.green, ConsoleUtils.Stiles.bold, "ALL MOTOR RESETS DONE READY FOR USE!", ConsoleUtils.Colors.reset)
