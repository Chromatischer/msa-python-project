from ftrobopy import *


class TxtStickInput:
    _pos_L_X = None
    _pos_L_Y = None
    _pos_R_X = None
    _pos_R_Y = None
    _txt = None
    _ir_stick_l = None
    _ir_stick_r = None
    _ir_button_l = None
    _ir_button_l_state = None
    _ir_button_r = None
    _ir_button_r_state = None

    _set_auto_update = False

    def __init__(self, txt: ftrobopy, set_auto_update=False):
        self._pos_L_X = 0
        self._pos_L_Y = 0
        self._pos_R_X = 0
        self._pos_R_Y = 0
        self._ir_button_l_state = False
        self._ir_button_r_state = False
        self._txt = txt
        self._ir_stick_l = self._txt.joystick(0, 0, 0)  # joystick objekt einer beliebigen ir-Fernbedienung (links)
        self._ir_stick_r = self._txt.joystick(1, 0, 0)  # joystick object einer beliebigen ir-Fernbedienung (rechts)
        self._ir_button_l = self._txt.joybutton(0, 0)
        self._ir_button_r = self._txt.joybutton(1, 0)

        self._set_auto_update = set_auto_update

    def updateValues(self):
        """
        updates all the internal values
        :return:
        """
        self._pos_L_X = self._ir_stick_l.leftright()
        self._pos_L_Y = self._ir_stick_l.updown()

        self._pos_R_X = self._ir_stick_r.leftright()
        self._pos_R_Y = self._ir_stick_r.updown()

        self._ir_button_l_state = self._ir_button_l.pressed()
        self._ir_button_r_state = self._ir_button_r.pressed()

    def getPos(self, stick="left", axis="X"):
        """
        returns a value between -1 and 1 as a **float** for the input of the specified stick and axis
        :param stick: the stick to get the pos of either left or right
        :param axis: the axis to get the value of the stick of either X or Y
        :return: a value between -1.0 and 1.0 as a float
        """

        if self._set_auto_update:
            self.updateValues()

        if stick is "left":
            if axis is "X":
                return self._pos_L_X
            elif axis is "Y":
                return self._pos_L_Y
            else:
                raise ValueError("axis is neither X or Y")
        elif stick is "right":
            if axis is "X":
                return self._pos_R_X
            elif axis is "Y":
                return self._pos_R_Y
            raise ValueError("axis is neither X or Y")
        else:
            raise ValueError("stick is neither left or right")

    def getButton(self, button="left"):
        """
        returns the boolean state for the specified button on the ir-remote
        :param button: either left or right
        :return: the boolean state of the specified button
        """
        if self._set_auto_update:
            self.updateValues()

        if button is "left":
            return self._ir_button_l_state
        elif button is "right":
            return self._ir_button_r_state
        else:
            raise ValueError("button is neither left or right")

    def getAllValuesAsStr(self):
        """
        returns all the values of the
        :return:
        """
        ret_str: str

        ret_str = str(self.getPos("left", "X")) + " " + str(self.getPos("left", "Y")) + " " + str(self.getPos("right", "X")) + " " + str(self.getPos("right", "Y")) + " " + str(self.getButton("left")) + " " + str(self.getButton("right"))

        return ret_str
