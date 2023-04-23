from TxtStickInput import *
from ftrobopy import *
from SimpleTxtConnector import *


if __name__ == "__main__":

    stxtc = SimpleTxtConnector()
    txtstinp = TxtStickInput(stxtc.txt, True)
    while True:
        print(txtstinp.getAllValuesAsStr())
