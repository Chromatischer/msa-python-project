from SimpleTxtConnector import *

# this script allows for quick and efficient tests of the switches to either confirm order or test functionality
# it does run slow, but that is acceptable (just hold the switch for long enough)

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    txt = stxtc.txt
    last1 = False
    last2 = False
    last3 = False
    last4 = False
    last5 = False
    last6 = False
    last7 = False
    last8 = False
    while True:
        if txt.input(1).state() is not last1:
            last1 = txt.input(1).state()
            if last1:
                print("state 1!")

        if txt.input(2).state() is not last2:
            last2 = txt.input(2).state()
            if last2:
                print("state 2!")

        if txt.input(3).state() is not last3:
            last3 = txt.input(3).state()
            if last3:
                print("state 3!")

        if txt.input(4).state() is not last4:
            last4 = txt.input(4).state()
            if last4:
                print("state 4!")

    #   if txt.input(5).state() and not last5:
    #       last5 = txt.input(5).state()
    #       print("state 5!")

        if txt.input(6).state() is not last6:
            last6 = txt.input(6).state()
            if last6:
                print("state 6!")

        if txt.input(7).state() is not last7:
            last7 = txt.input(7).state()
            if last7:
                print("state 7!")

        if txt.input(8).state() is not last8:
            last8 = txt.input(8).state()
            if last8:
                print("state 8!")
