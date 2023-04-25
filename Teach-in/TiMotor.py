import ftrobopy


class TiMotor(object):

    def __init__(self, txt: ftrobopy, motnum: int, min_spd: int, max_spd: int, verbose: bool = False):
        self.txt = txt
        self.mot = txt.motor(motnum)
        self._last_counter: int = 0
        self._true_position: int = 0
        self._min_speed: int = min_spd
        self._max_speed: int = max_spd
        self._verbose: bool = verbose
        self._current_spd: int = 0

    def getTruePosition(self):
        return self._true_position

    def resetTruePosition(self):
        if self._verbose:
            print("Before: ", self._true_position)
        self._true_position = 0
        self._last_counter = 0
        if self._verbose:
            print("After: ", self._true_position)

    def move(self, p: float):
        if p > 1.0 or p < -1.0:
            raise ValueError("p out of bounds!")
        if p != 0:
            if p > 0:
                if self._max_speed * p < self._min_speed:
                    self._current_spd = self._min_speed
                else:
                    self._current_spd = round(self._max_speed * p)
                self._true_position = self._last_counter + self.mot.getCurrentDistance()
            elif p < 0:
                if self._max_speed * p > -self._min_speed:
                    self._current_spd = -self._min_speed
                else:
                    self._current_spd = round(self._max_speed * p)
                self._true_position = self._last_counter - self.mot.getCurrentDistance()
            self.mot.setSpeed(self._current_spd)
        else:
            if self._verbose:
                print("dbg last counter: ", self._last_counter, " current position: ", self._true_position, " dbg motor current distance: ", self.mot.getCurrentDistance(), " dbg motor current spd: ", self._current_spd)

            self._last_counter = self._true_position
            self.mot.stop()

            i = 0
            while not self.mot.getCurrentDistance() == 0:
                self.txt.updateWait()
                i += 1
                if i > 100:
                    raise Exception("unable to verify motor reset! After 100 cycles!")
