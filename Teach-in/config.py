from ftrobopy import *


class ConfigPy:
    min_speed_m1 = 410
    max_speed_m1 = 512
    min_speed_m2 = 0
    max_speed_m2 = 512
    min_speed_m3 = 0
    max_speed_m3 = 512
    min_speed_m4 = 300
    max_speed_m4 = 100


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
