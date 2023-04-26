class TiPosition:
    """
    this class is used to save and retrieve the position data for the txt-model
    """

    def __init__(self, m1: int, m2: int, m3: int, m4: int):
        self._pos = [0, 0, 0, 0]
        self._pos[0] = m1
        self._pos[1] = m2
        self._pos[2] = m3
        self._pos[3] = m4

    def get(self, motor):
        return self._pos[motor-1]

    def set(self, motor, value):
        self._pos[motor-1] = value

    def get_str(self):
        string: str = 'm1: [' + str(self._pos[0]) + '] m2: [' + str(self._pos[1]) + '] m3: [' + str(self._pos[2]) + '] m4: [' + str(self._pos[3]) + ']'
        return string
