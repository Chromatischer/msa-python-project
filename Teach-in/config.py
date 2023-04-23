from ftrobopy import *


class ConfigPy:
    speedM1 = 512
    speedM2 = 512
    speedM3 = 512
    speedM4 = 512

    @staticmethod
    def set_default_config(txt: ftrobopy):
        M = [txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR, txt.C_MOTOR]
        I = [(txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_RESISTOR, txt.C_ANALOG),
             (txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_SWITCH, txt.C_DIGITAL),
             (txt.C_SWITCH, txt.C_DIGITAL)]
        txt.setConfig(M, I)
        txt.updateConfig()
