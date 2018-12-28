from tkinter import Tk

from Countdown import create_logger
from .SmartKinter import SmartLabel, SmartButton
from .input_windows import TimeCalculator, TimeInput

logger = create_logger('TT')


class TimeTest(Tk):
    """A Test class for testing the TimeInput and TimeCalculator functions"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.sec = 0
        self.lbl = SmartLabel(self, text='0 Seconds')
        self.lbl2 = SmartLabel(self, text='0 Seconds')
        self.lbl.grid(columnspan=2)
        self.lbl2.grid(row=1, columnspan=2)
        self.btn1 = SmartButton(self, text='Input And Change Time', command=self.get_and_change_time)
        self.btn1.grid(row=2)
        self.btn2 = SmartButton(self, text='Quit', command=self.destroy)
        self.btn2.grid(row=2, column=1)

    def get_and_retrieve_time(self):
        """Gets the time with a timeinput and retrieves the seconds from the TimeInput class"""
        self.inp = TimeInput()
        self.inp.mainloop()
        logger.debug('Finished mainloop.')
        logger.debug('Seconds: %s', self.inp.secs)
        self.TC = TimeCalculator(self.inp.secs)
        logger.debug('Formatted string: %s', self.TC.wordstr)

    def get_and_change_time(self):
        """Preforms get_and_retrieve_time and changes the labels with the seconds and formatted string."""
        self.get_and_retrieve_time()
        self.lbl.config(text='%d Seconds' % self.inp.secs)
        logger.debug('Configed? first label')
        self.lbl2.config(text=self.TC.wordstr)
        logger.debug('Configed? second label')
