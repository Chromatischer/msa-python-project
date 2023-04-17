from ftrobopy import *


class ConfigPy:
    speedM1 = 100
    speedM2 = 100
    speedM3 = 100
    speedM4 = 100

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
