"""This module is to make updated classes of certain Tkinter classes that do certain functions on their own,
such as set the default font and pack at the end of the parent __init__ function."""

import tkinter  # obviously we can't make tkinter classes without the tkinter module


class SmartLabel(tkinter.Label):  # The label is smart because it does stuff on it's own
    """A Smart Tkinter Label. Automatically packs the label and sets the font to the given font, which also defaults
    to font size 24."""

    def __init__(self, master=None, FONT='Courier New', font_size: int = 24, **kw) -> None:
        """
        Initializes the class

        :param master: ???
        :param cnf: ???
        :param FONT: The font family to use
        :param font_size: The size to make the font
        :param kw: The optional args that are not explicitly listed.
        :type master: ???
        :type cnf: ???
        :type FONT: str
        :type font_size: int
        :type kw: Any
        """
        super().__init__(master, font=(FONT, font_size), **kw)


class SmartButton(tkinter.Button):
    """A Smart Button. Automatically sets the button text font and packs it. The default font size is 16. The setup
    for it is essentially identical to the setup of the SmartLabel. """

    def __init__(self, master=None, FONT='Courier New', font_size: int = 12, **kw) -> None:
        """
        Initializes the class

        :param master: ???
        :param cnf: ???
        :param FONT: The font family to use
        :param font_size: The size to make the font
        :param kw: The optional args that are not explicitly listed.
        :type master: ???
        :type cnf: ???
        :type FONT: str
        :type font_size: int
        :type kw: Any
        """
        super().__init__(master, font=(FONT, font_size), **kw)


class SmartEntry(tkinter.Entry):
    """A Smart Entry. Automatically sets font."""

    def __init__(self, master=None, FONT='Courier New', font_size: int = 12, **kw) -> None:
        """
        Initializes the class

        :param master: ???
        :param cnf: ???
        :param FONT: The font family to use
        :param font_size: The size to make the font
        :param kw: The optional args that are not explicitly listed.
        :type master: ???
        :type cnf: ???
        :type FONT: str
        :type font_size: int
        :type kw: Any
        """
        super().__init__(master, font=(FONT, font_size), **kw)

    def grid(self, **kwargs):
        super().grid(padx=2, **kwargs)
