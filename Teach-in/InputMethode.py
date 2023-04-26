class InputMethode(object):
    """
    defines the input methode for the Ti-Controller
    """
    _inputMethode: str = None

    def __init__(self, args: [str]):
        if len(args) != 1:
            raise Exception("too many arguments")

        print(args[0])
        if str(args[0]) != "joystick" and str(args[0]) != "file":
            raise ValueError(str(args[0]), "is not one of: 'joystick' or 'file'")
        else:
            self._inputMethode = str(args[0])

    def getInputMethode(self):
        """
        gets the currently selected input methode if the local variable is not an option throws: ValueError
        :raises:  when the data in the variable is none of the two possibilities
        :return: the string value of the selected input methode either joystick or file
        """

        if self._inputMethode is "joystick" or "file":
            return self._inputMethode
        else:
            raise ValueError("variable inputMethode does not have expected value!")

    def setInputMethode(self, input_methode: str):
        """
        sets the input methode to the given value if possible, else throws ValueError
        :param input_methode: the name of the new input methode (one of: 'joystick' or 'file')
        :return:
        """
        if input_methode is "joystick" or "file":
            self._inputMethode = input_methode
        else:
            raise ValueError("input parameter does not have expected value!")

    def setInputMethode_int(self, input_methode: int):
        """
        sets the input methode to the given value if possible, else throws ValueError
        :param input_methode: the name of the new input methode (1 = joystick, 2 = file)
        :return:
        """
        if input_methode is 1 or 0:
            if input_methode == 1:
                self._inputMethode = "joystick"
            elif input_methode == 0:
                self._inputMethode = "file"
        else:
            raise ValueError("input parameter does not have expected value!")

    def switch(self):
        """
        toggles between one of the two possible input types
        :return:
        """
        if self._inputMethode is "joystick":
            self._inputMethode = "file"
        elif self._inputMethode is "file":
            self._inputMethode = "joystick"
        else:
            raise ValueError("internal error internal variable does not have expected value!")
