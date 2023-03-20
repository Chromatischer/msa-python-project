class Position:
    """
    this class is used to save and retrieve the position data for the txt-model
    """
    _pos = {}

    def __init__(self, m1: int, m2: int, m3: int, m4: int):
        self._pos['m1'] = m1
        self._pos['m2'] = m2
        self._pos['m3'] = m3
        self._pos['m4'] = m4

    def __getattr__(self, motor):
        return self._pos[motor]

    def __setattr__(self, motor, value):
        self._pos[motor] = value

    def __resetattr__(self, m1: int, m2: int, m3: int, m4: int):
        self._pos['m1'] = m1
        self._pos['m2'] = m2
        self._pos['m3'] = m3
        self._pos['m4'] = m4
