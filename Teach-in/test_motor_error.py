from TiModel import *
from SimpleTxtConnector import *
#DISCLAIMER:
# this script does not rally work, but it fulfilled its purpose in helping me understand the issue better! Just don't use it!

if __name__ == "__main__":
    ftxt = SimpleTxtConnector().txt
    tim = TiModel(ftxt, False)

    tim.TestMotors.Reset.m1()
    #tim.TestMotors.Reset.m4()

    for i in range(1):
        print("  running: ", i, " out of: 1")
        while not tim.getCounterValue(1) <= -100:
            tim.MovementAgent.DirectControl.Safe.m4(0)
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: -100, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) >= 0:
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: 0, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) <= -300:
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: -300, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) >= 0:
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: 0, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) <= -200:
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: -200, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) >= 0:
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: 0, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) <= -500:
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: -500, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) >= 200:
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: 200, got: ", tim.getCounterValue(1))
        while not tim.getCounterValue(1) >= 0:
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
        print("expected: 0, got: ", tim.getCounterValue(1))
    ftxt.stopOnline()
    exit()


    for i in range(20):
        while not tim.getCounterValue(1) <= -i * 25:
            # print(-i * 25, " ", tim.getCounterValue(1), " \r")
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
    for i in range(20):
        while not tim.getCounterValue(1) >= -900 + (i * 25):
            # print(-925 + (i * 25), " ", tim.getCounterValue(1), " \r")
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)

    for i in range(32):
        while not tim.getCounterValue(4) <= -i * 25:
            print(-i * 25, " ", tim.getCounterValue(4), " \r")
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)

    for i in range(32):
        while not tim.getCounterValue(4) >= -925 + (i * 25):
            print(-925 + (i * 25), " ", tim.getCounterValue(4), " \r")
            tim.MovementAgent.DirectControl.Safe.m1(1)
        tim.MovementAgent.DirectControl.Safe.m1(0)
