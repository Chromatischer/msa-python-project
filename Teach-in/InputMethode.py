class InputMethode(object):
    """
    defines the input methode for the Ti-Controller
    """
    valid_methods = ["curses", "joystick", "file"]
    _inputMethode: str = None

    def __init__(self, args: [str]):
        if len(args) != 1:
            raise Exception("too many arguments")

        print(args[0])
        if str(args[0]) not in self.valid_methods:
            raise ValueError(str(args[0]), "is not one of: " + self.valid_methods)
        else:
            self._inputMethode = str(args[0])

    def getInputMethode(self):
        """
        gets the currently selected input methode if the local variable is not an option throws: ValueError
        :raises:  when the data in the variable is none of the two possibilities
        :return: the string value of the selected input methode either joystick or file
        """

        if self._inputMethode in self.valid_methods:
            return self._inputMethode
        else:
            raise ValueError("variable inputMethode does not have expected value!")

    def setInputMethode(self, input_methode: str):
        """
        sets the input methode to the given value if possible, else throws ValueError
        :param input_methode: the name of the new input methode (one of: valid_methods)
        :return:
        """
        if input_methode in self.valid_methods:
            self._inputMethode = input_methode
        else:
            raise ValueError("input parameter does not have expected value!")

    def setInputMethode_int(self, input_methode: int):
        """
        sets the input methode to the given value if possible, else throws ValueError
        :param input_methode: the name of the new input methode (0 = curses, 1 = joystick, 2 = file)
        :return:
        """
        if input_methode in range(2):
            self._inputMethode = self.valid_methods[input_methode]
        else:
            raise ValueError("input parameter does not have expected value!")

    def switch(self):
        """
        toggles between one of the possible input types
        :return:
        """
        if self._inputMethode is "joystick":
            self._inputMethode = "file"
        elif self._inputMethode is "file":
            self._inputMethode = "curses"
        elif self._inputMethode is "curses":
            self._inputMethode = "file"
        else:
            raise ValueError("internal error internal variable does not have expected value!")
