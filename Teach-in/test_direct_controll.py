from SimpleTxtConnector import *
from TiModel import *
from TxtStickInput import *

# this script allows for quick use of the txt-ir-remote to control each of the motors separately
# it too performs as a test script for the motor control of the TiModel.py

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    txsticki = TxtStickInput(stxtc.txt, True)
    txtim = TiModel(stxtc.txt)

    if txsticki.getPos("left", "Y") != 0:
        txtim.MovementAgent.DirectControl.Unsafe.move_m2(txsticki.getPos("left", "Y"))
    else:
        stxtc.txt.motor(2).stop()

    if txsticki.getPos("right", "X") != 0:
        txtim.MovementAgent.DirectControl.Unsafe.move_m3(txsticki.getPos("right", "X"))
    else:
        stxtc.txt.motor(3).stop()

    if txsticki.getPos("right", "Y") != 0:
        txtim.MovementAgent.DirectControl.Unsafe.move_m4(txsticki.getPos("right", "Y"))
    else:
        stxtc.txt.motor(4).stop()

    while True:
        if txsticki.getPos("left", "X") != 0:
            txtim.MovementAgent.DirectControl.Safe.move_m1(txsticki.getPos("left", "X"))
            print(stxtc.txt.motor(1).getCurrentDistance())


