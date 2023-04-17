
## Projektdokumentation:

- 25.11.22: 
    - Mogens: 
        - Import der Python library fuer das Programmieren [ftrobopy](https://github.com/ftrobopy/ftrobopy)
        - anfangen simple Sachen zu Programmieren]
        - Plan fuer umsteigen auf ftce [FT Community Edition](https://cfw.ftcommunity.de/ftcommunity-TXT/de/)
    - Abend:
        - versuchen txt mit FTCE zu flashen scheitert an der micro SD Card, bzw allen, die wir versucht haben zu verwenden.
        - schreiben des `cheksys.py` files und des `nbc.py` files fuer keyinterrupts.
            - importierbar siehe unten!
        - hilfe kommt aus dem `TXTwithPython.pdf`
        - endlich SD Card gefunden sie funktioniert
            - scheint langsam zu sein, trozdem hat der TXT Controller angefangen zu Booten!
- 26.11.22
    - Morgens:
        - ausbauen des TXT controllers zum installieren der Community Firmware
        - Papa hat die Community Firmware zum Laufen bekommen!
    - Mittags:
        - einbauen des TXTs und testen der ersten Programme!
        - Problem:
            - Programm nicht ausfuehrbar, da viele Fehler, warscheinlich wegen keiner Verbindung zum TXT
            ```
            TimeoutError: timed out
            ```
            - Angepingt unter:
            ```python
            ft_txt = ftrobopy.ftrobopy('192.186.7.2', 65000) #Standart fuer USB connection
            ```
            - Problem auf morgen verschoben
- 27.11.22
    - Morgens:
        - versuchen den Txt anzusprechen
        - Ports ueberprueft... meiner ist nicht offen
    - Nachmittags:
        - Papa hat Anleitung gelesen!
            -   1. um per USB zu funktionieren muss die App `FT GUI` geoeffnet werden
                2. der richtige Code zum Connecten ist jetzt: 
                ```py 
                txt = ftrobopy.ftrobopy('ft-txt', 65000) # gilt fuer das Netzt zu Hause
                ```
                3. wie / ob USB funktioniert weiss ich immernoch nicht!
        - ausfuehren und Testen des ersten Programms `testUSB.py`
        - schreiben des Programmes `irTest.py` zum Testen der Fernbedienung
        - schreiben des Programmes `sensorTest.py` zum Herausfinden, welche Inputs was tun!
            - Umbenannt in `sensoMotoTest.py` kann jetzt auch Motoren in startpos fahren!
            - Experimientieren mit "Coprocesses" -> nicht erfolgreich
            - Schreiben dieses netten Programms hier:
            ```python
            IR = txt.getCurrentIr()
            if IR[0]:
                m4.setSpeed(IR[0]*34)
                txt.updateWait(0.5)
            if IR[1]:
                m1.setSpeed(IR[1]*34)
                txt.updateWait(0.5)
            if IR[2]:
                m3.setSpeed(IR[2]*34)
                txt.updateWait(0.5)
            motorstopAll() #funktion stoppt alle Motoren
            ```
            Problem hiermit: sehr langsam und rucklig (einfach scheisse!) -> muesste mit Nebenlaeufiggkeit geloest werden! Kann ich Nebenlaeufigkeit? Immernocht: NEIN!
    - Abends:
        - der Txt hat aufgehoert ueber Internet sich zu Verbinden...
            - hat sich einfach wieder verbunden, kein Plan was schief ging!
        - weiterarbeiten an der Motorenansteuerung via IR-Fernbedienung!
        - Code in `irTest.py` von: [StackOverflow](https://stackoverflow.com/questions/61626953/python-printing-an-ascii-cartesian-coordinate-grid-from-a-2d-array-of-position)
            - dieser hier: 
            ```python
            def stickPos():
                if (stickLX != txt.getCurrentIr().__getitem__(0) +5) | (stickLY != txt.getCurrentIr().__getitem__(1) +5):
        
                # prepare the empty content
                rows = 11
                cols = 11
                content = [["."]*cols for _ in range(rows)]
                content[stickLY][stickLX]  = "O"
                # build frame
                width       = len(str(max(rows,cols)-1))
                contentLine = "values"
                

                #   print grid
                for i,row in enumerate(reversed(content),1):
                    values = " ".join(f"{v:{width}s}" for v in row)
                    line   = contentLine.replace("values",values)
                print(line)
                print()
                txt.updateWait()
            ```
        - zu Ende programmieren des coolen GUIs -> es ist fett unnoetig hat aber spass gemacht!
        - so sieht einer der virtuellen Sticks jetzt aus!
        ```
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  O  .  .  .  .  .
        -  -  -  -  -  +  -  -  -  -  -
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  .  .
        .  .  .  .  .  |  .  .  .  0  1
        ```
- 28.11.22
  - Morgens:
  - Feststellen, das ich unbedingt Nebenlaeufigkeit brauche
  - weiterschreiben an `sensoMotoTest.py`
  - Nachmittags:
  - nach nur knapp einer Stunde habe ich auch multithreading zum laufen bekommen!
    - Ich habe es dann [hier](https://www.python-forum.de/viewtopic.php?t=7081) verstanden / rauskopiert!
    - warum tue ich mir das an?
    ```python
    import time
    import _thread
    def one():
        while True:
            time.sleep(1)
            print("one")

    def two():
        while True:
            time.sleep(1)
            print("two")

    _thread.start_new_thread(one, ())
    two()
    ```
    output:
    ```
    one
    two
    one
    two
    ```
    - jetzt wo wir also wissen, wie multithreading geht, lass es uns implementieren!
        - Problem: es laeuft zu langsam -> der Zaehler ist nicht schnell genug! Deswegen sehe ich da momentan schwoarz! siehe `coprocessTest.py`
    - ich war mal hier:
    ```python
    if __name__ == '__main__':
        q = mp.Queue()
        print("debug")
        p = Process(target=m1Counter, args=(q,))
    
        print("debug2")
        p.start()
        print(q.get())
        p.join()
    ```
    - habe das alles geloescht und bin wieder 45min frueher angekommen!
- 29.11.22
  - Morgens: 
    - schreiben des Programmes `motorTet.py`
  - Mittags:
    - testen des Programmes
    - zerbrechen der Lichtdurlassenden Scheibe!
- 30.11.22
  - Morgens:
    - anfangen des Umbaus des rechten Schneckenmotors
  - Mittags:
    - umbauen des gesammten Projekts 
  - Nachmittags:
    - Fertig mit umbau!
- 4.1.23
  - Abends:
    - schreiben des Programmes ```lichtschrankentest.py``` zum Testen des analogen Zaehlens
    - weitere Schritte: habe ich vergessen
    - anfangen pyqt installation
- 22.1.23
  - Abends:
    - nach mehreren Stunden funktioniert das Programm ```test.py```
    - ich musste:
      1. homebrew installieren
      2. die default installation von python auf den richtigen path aendern
      3. ftcommunity-txt herrunterladen und verschiedene Datein (```laucher.py```, ```logger.py```, ```touch_keyboard.py```, ```TxtStyle.py```, ```TouchStyle.pt```und den ```themes``` ordner in dieses Verzeichnis kopieren.)
      4. hier gibt es aber beim Ausfuehren von ```test.py``` ein Problem: das Fenster ist immer fullscreen.
            - der Problemcode dafuer ist:
         ```python
            def getScreenSize():
                if 'SCREEN' in os.environ:
                    (w, h) = os.environ.get('SCREEN').split('x')
                    return QSize(int(w), int(h))

                if IS_ARM:
                    return QApplication.desktop().screenGeometry().size()

                if DEV_ORIENTATION == "LANDSCAPE":
                    return QSize(320, 240)

                return QSize(240, 320)
            ```
            hier war das Problem: erst wurde auf ARM prozessor gecheckt, da der TXT einen solchen hat (Ich leider auch deswegen fullscreen) jetzt konnte ich aber einfach die ```SCREEN``` variable nach oben nehmen und es funktioniert so maeh!
- 12.2.23
  - Mittags:
    - finden des Problems in ```Touchstyle.py``` welches dafür sorgt, dass es immer full-screen ist!
    ```python
    # TXT windows are always fullscreen on arm (txt itself)
    # and windowed else (e.g. on PC)
    def show(self):
        if IS_ARM and not DEV:
            QWidget.showFullScreen(self)
        else:
            QWidget.show(self)
        # send a message to the launcher once the main widget has been
        # drawn for the first time
        self.notify_launcher()
    ```
    - problem wurde behoben durch Verwendung von der TXT und TXPI variable, die explizit und nicht implizit einen TXT anzeigt!
    ```python
    #das hier ist jetzt nur ein Beispiel, nicht der gleiche Code wie Oben
    #zeigt aber die Verwengung von TXT und TXPI anstelle von IS_ARM
    
    if TXT or TXPI:
        return QApplication.desktop().screenGeometry().size()

    if 'SCREEN' in os.environ:
        (w, h) = os.environ.get('SCREEN').split('x')
        return QSize(int(w), int(h))

    if DEV_ORIENTATION == "LANDSCAPE":
        return QSize(320, 240)

    return QSize(240, 320)
    ```
  - 19.1.23
    - Abends:
      - schreiben des Programms: ```Countertest.py``` zum Testen der Counterfunktion des TXT! (Fehler lag in der Verkabelung, des Counter-motors siehe Foto → dort Beispiel richtig)
      - created pull-request: [247](https://github.com/ftCommunity/ftcommunity-TXT/pull/247) on Github to be reviewed!
## Andere wichtge Infos:
  python qt test recherge website:
   - https://docs.python.org/3/library/unittest.html
### Hardware:
zum Verkabeln eines Zaehlermotors mit dem TXT muss das Rote-Kabel an 9V angeschlossen werden, das Schwarze-Kabel kommt an den C1-Port, NICHT DER MIT **T** das Gruene-Kabel kommt an den Masse anschluss (T) 
## Programmausschnitte:
Belegung Input:
1. Winde Links
2. Drehturm
3. Winde Rechts
4. Greifer rechts
5. Drehsensor links
6. NOT AUS!

Belegung Output:
1. Schneckenmotor rechts + ist runter (Minimalspeed: 340)
2. Scheckenmotor links + ist runter   (Minimalspeed: 340)
3. Greifmotor + ist zu
4. Drehmotor + ist im Uhrzeigersinn (Minimalspeed: 170)

Programm um die Fernbedienung abzufragen:
```python
def StatusIR(input):
    #----------------------------------------------------
    # How to read the sequence for the infrared data?
    # For the default dip switch setting, only indices
    # 0 to 5 are relevant. Other indices become relevant
    # for other settings of the dipswitches.
    # 0 > LEFT stick: left-right -15 to 15
    # 1 > LEFT stick: up-down -15 to 15
    # 2 > RIGHT stick: left-right -15 to 15
    # 3 > RIGHT stick: up-down -15 to 15
    # 4 > On button: 1, Off button 2
    #----------------------------------------------------
    if input[0]: #LEFT STICK LEFT-RIGHT
        if input[0] > 0:
            print("left stick right: {:5d}".format(input[0]))
        else:
            print("left stick left: {:5d}".format(input[0]))
    if input[1]: #LEFT STICK UP-DOWN
        if input[1] > 0:
            print("left stick up: {:5d}".format(input[1]))
        else:
            print("left stick down: {:5d}".format(input[1]))
    if input[2]: #RIGHT STICK LEFT-RIGHT
        if input[2] > 0:
            print("right stick right: {:5d}".format(input[2]))
        else:
            print("right stick left: {:5d}".format(input[2]))
    if input[3]: #RIGHT STICK UP-DOWN
        if input[3] > 0:
            print("right stick up: {:5d}".format(input[3]))
        else:
            print("right stick down: {:5d}".format(input[3]))
    if input[4]: #ON-OFF PRESSED-DEPRESSED
        if input[4] == 1:
            print("On Button: {:5d}".format(input[4]))
        if input[4] == 2:
            print("Off Button: {:5d}".format(input[5]))
```
Bessere Version des gleichen Programm:
```python
def StatusIR(input):
    global input0
    global input1
    global input2
    global input3
    global input4
    #----------------------------------------------------
    # How to read the sequence for the infrared data?
    # For the default dip switch setting, only indices
    # 0 to 5 are relevant. Other indices become relevant
    # for other settings of the dipswitches.
    # 0 > LEFT stick: left-right -15 to 15
    # 1 > LEFT stick: up-down -15 to 15
    # 2 > RIGHT stick: left-right -15 to 15
    # 3 > RIGHT stick: up-down -15 to 15
    # 4 > On button: 1, Off button 2
    #----------------------------------------------------
    if input[0]: #LEFT STICK LEFT-RIGHT
        if input[0] != input0:
            if input[0] > 0:
                print("left stick right: {:5d}".format(input[0]))
            else:
                print("left stick left: {:5d}".format(input[0]))
            input0 = input[0]
    if input[1]: #LEFT STICK UP-DOWN
        if input[1] != input1:
            if input[1] > 0:
                print("left stick up: {:5d}".format(input[1]))
            else:
                print("left stick down: {:5d}".format(input[1]))
            input1 = input[1]
    if input[2]: #RIGHT STICK LEFT-RIGHT
        if input[2] != input2:
            if input[2] > 0:
                print("right stick right: {:5d}".format(input[2]))
            else:
                print("right stick left: {:5d}".format(input[2]))
        input2 = input[2]
    if input[3]: #RIGHT STICK UP-DOWN
        if input[3] != input3:
            if input[3] > 0:
                print("right stick up: {:5d}".format(input[3]))
            else:
                print("right stick down: {:5d}".format(input[3]))
        input3 = input[3]
    if input[4]: #ON-OFF PRESSED-DEPRESSED
        if input[4] != input4:
            if input[4] == 1:
                print("On Button: {:5d}".format(input[4]))
            if input[4] == 2:
                print("Off Button: {:5d}".format(input[5]))
        input4 = input[4]
```
Programm fuer Console die Key-Inputs abfaengt:
```python
from nbc import NonBlockingConsole #nbc ist eine py Datei, die muss anbei liegen!
    with NonBlockingConsole() as nbc:
    if nbc.get_data() == '\x1b': #das ist ESC
        print("stopped because escape was pressed!")
        txt.stopOnline()
        os._exit(1)
```
Programm um die Motoren auf Startposition zu fahren:
```python
def resetMotorPos(motor):
    if motor == 1:
        print('Motor m1 auf Statrposition fahren!')
        while i3.state() != 1:
            m1.setSpeed(-512)
        m1.stop()
        print ('Motor m1 auf Startposition!')
    if motor == 2:
        print('Motor m2 auf Startposition fahren!')
        #while i1.state() != 1:
            #m2.setSpeed(-512)
        #m2.stop()
        print ('Motor m2 auf Startposition!')
    if motor == 3:
        print('Motor m3 auf Startposition fahen!')
        while i7.state() != 1:
            m3.setSpeed(-512)
        m3.stop()
        print('Motor m3 auf Startposition!')
    if motor == 4:
        print('Motor m4 auf Startposition fahren!')
        while i2.state() != 1:
            m4.setSpeed(512)
        m4.stop()
        print("Motor m4 auf Startposition!")
```



ftcommunity-TXT/board/fischertechnik/TXT/rootfs/opt/ftc/
