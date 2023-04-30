from SimpleTxtConnector import *
if __name__ == "__main__":
    txt = SimpleTxtConnector().txt

    m1 = txt.motor(1)
    m4 = txt.motor(4)
    print(m1.getCurrentDistance())
    print(m4.getCurrentDistance())

    while m1.getCurrentDistance() < 100:
        m1.setSpeed(-512)
    m1.stop()

    while m4.getCurrentDistance() < 100:
        m4.setSpeed(-512)
    m4.stop()

    print(m1.getCurrentDistance())
    print(m4.getCurrentDistance())
    i = 0
    while m1.getCurrentDistance() != 1 and m4.getCurrentDistance() != 1:
        txt.incrCounterCmdId(0)
        txt.incrCounterCmdId(3)
        txt.updateWait(0.1)
        i += 1
        if i > 100:
            txt.stopOnline()
            raise OSError("lol")
    while m1.getCurrentDistance() < 100:
        m1.setSpeed(512)
    m1.stop()

    while m4.getCurrentDistance() < 100:
        m4.setSpeed(512)
    m4.stop()

    print("i", i)
    print(m1.getCurrentDistance())
    txt.stopOnline()
