from SimpleTxtConnector import *

if __name__ == "__main__":
    stxtc = SimpleTxtConnector()
    txt = stxtc.txt
    print(txt.getVersionNumber())
    txt.stopOnline()
    print(stxtc)
