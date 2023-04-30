from TiModel import *
from SimpleTxtConnector import *
#DISCLAIMER:
# this script does not rally work, but it fulfilled its purpose in helping me understand the issue better! Just don't use it!

if __name__ == "__main__":
    ftxt = SimpleTxtConnector().txt
    tim = TiModel(ftxt, False)

    tim.TestMotors.Reset.m1()
    tim.TestMotors.Reset.m4()
    for i in range(37):
        while not tim.getCounterValue(1) <= -i * 25:
            print(-i * 25, " ", tim.getCounterValue(1), " \r")
            tim.MovementAgent.DirectControl.Safe.m1(-1)
        tim.MovementAgent.DirectControl.Safe.m1(0)

    for i in range(37):
        while not tim.getCounterValue(1) >= -925 + (i * 25):
            print(-925 + (i * 25), " ", tim.getCounterValue(1), " \r")
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
