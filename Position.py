class Position:
    """
    this class is used to save and retrieve the position data for the txt-model
    """
    pos = {}

    def __init__(self, m1: int, m2: int, m3: int, m4: int):
        self.pos['m1'] = m1
        self.pos['m2'] = m2
        self.pos['m3'] = m3
        self.pos['m4'] = m4

    def __getattr__(self, motor):
        return self.pos[motor]

    def __setattr__(self, motor, value):
        self.pos[motor] = value
