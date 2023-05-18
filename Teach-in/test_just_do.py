from SimpleTxtConnector import *

#----------------------------------------------------JUST DO-----------------------------------------------------------#
#       dieses Script erlaubt klartext steuerung des Modells. Die gewünschte Richtung angeben (hoch, runter,           #
#    links, rechts, vor, zurueck) eine Zeit in Sekunden und eine Motorgeschwindigkeit dann das Programm ausführen,     #
#         sobald eine Verbindung zum TXT besteht, wird der Befehl **OHNE** sicherheitsfunktionen ausgeführt            #
#----------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    richtung: str = "links"  # die richtung, in welche das Modell sich bewegen soll!

    time: float = 3.0  # die Zeit in sek, welche mindestens vergehen soll, bis der Motor stoppt!

    # **ACHTUNG: ES GIBT KEINE SICHERHEITSVORKEHRUNGEN, ES BESTEHT ZERSTÖRUNGSRISIKO**
    
    speed: int = 512  # die Geschwindigkeit, mit der sich der Motor bewegen soll!

    safety: bool = True  # verhindert das ungewollte Ausführen des Programms muss auf True gesetzt werden!
    
    print("bewege: ", richtung, " für: ", str(time), " sekunden mit geschwindigkeit: ", str(speed))

    #region program!
    stxtc = SimpleTxtConnector()
    txt = stxtc.txt

    m1 = txt.motor(1)
    m2 = txt.motor(2)
    m3 = txt.motor(3)
    m4 = txt.motor(4)

    if safety:

        if richtung == "links":
            m4.setSpeed(speed)
            txt.updateWait(time)
            m4.stop()

        if richtung == "rechts":
            m4.setSpeed(-speed)
            txt.updateWait(time)
            m4.stop()

        if richtung == "zurueck":
            m1.setSpeed(speed)
            txt.updateWait(time)
            m1.stop()

        if richtung == "vor":
            m1.setSpeed(-speed)
            txt.updateWait(time)
            m1.stop()

        if richtung == "hoch":
            m2.setSpeed(speed)
            txt.updateWait(time)
            m2.stop()

        if richtung == "runter":
            m2.setSpeed(-speed)
            txt.updateWait(time)
            m2.stop()

        if richtung == "zu":
            m3.setSpeed(speed)
            txt.updateWait(time)
            m3.stop()

        if richtung == "auf":
            m3.setSpeed(-speed)
            txt.updateWait(time)
            m3.stop()
    #endregion
    txt.stopOnline()
    exit(0)
