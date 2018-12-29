"""This module is to make updated classes of certain Tkinter classes that do certain functions on their own,
such as set the default font and pack at the end of the parent __init__ function."""

import tkinter

from Countdown import create_logger

logger = create_logger('SK')


class LoggingGrid(tkinter.Grid):
    """A Grid system that logs all of it's arguments."""

    def grid(self, cnf=None, **kw):
        """The grid function. Logs the creation of a gris to DEBUG."""
        s = ''
        if cnf is None:
            cnf = {}
        for a, b in kw.items():
            s += '%s = %s,' % (a, b)
        logger.debug('Grid ran with arguments %s' % s)
        super().grid_configure(cnf, **kw)


class SmartLabel(tkinter.Label, LoggingGrid):
    """A Smart Tkinter Label. Automatically packs the label and sets the font to the given font, which also defaults
    to font size 24."""

    def __init__(self, master=None, FONT='Courier New', font_size: int = 20, **kw) -> None:
        """Initializes the class"""
        super().__init__(master, font=(FONT, font_size), **kw)
        if kw.get('text') is not None:
            logger.debug('Label with text %s was created', kw.get('text'))
        else:
            logger.debug('Label was created')


class SmartButton(tkinter.Button, LoggingGrid):
    """A Smart Button. Automatically sets the button text font and packs it. The default font size is 16. The setup
    for it is essentially identical to the setup of the SmartLabel. """

    def __init__(self, master=None, FONT='Courier New', font_size: int = 12, **kw) -> None:
        """Initializes the class"""
        if kw.get('command') is None:
            raise ValueError('No command for SmartButton. Keyword is command.')
        super().__init__(master, font=(FONT, font_size), **kw)
        if kw.get('text') is not None:
            logger.debug('Button with text %s and command with name %s was created', kw.get('text'),
                         kw.get('command').__name__)
        else:
            logger.debug('Button with command with name %s was created was created', kw.get('command').__name__)


class SmartEntry(tkinter.Entry, LoggingGrid):
    """A Smart Entry. Automatically sets font."""

    def __init__(self, master=None, FONT='Courier New', font_size: int = 12, **kw) -> None:
        """Initializes the class"""
        super().__init__(master, font=(FONT, font_size), **kw)
        logger.debug('A field was created.')

    def grid(self, **kwargs):
        super().grid(padx=2, **kwargs)
