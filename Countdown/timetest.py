from tkinter import Tk

from Countdown import create_logger
from .SmartKinter import SmartLabel, SmartButton
from .input_windows import TimeInput, DateInput
from .prefab import exit_widget

logger = create_logger('TT')


class TimeTest(Tk):
    """A Test class for testing the TimeInput and DateInput functions"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.sec = 0
        self.lbl = SmartLabel(self, text='0 Seconds')
        self.lbl2 = SmartLabel(self, text='0 Seconds')
        self.lbl.grid(columnspan=3)
        self.lbl2.grid(row=1, columnspan=3)
        self.btn1 = SmartButton(self, text='Input HH/MM/SS', command=lambda: self.get_and_change_time(TimeInput))
        self.btn1.grid(row=2)
        self.btn3 = SmartButton(self, text='Input Date', command=lambda: self.get_and_change_time(DateInput))
        self.btn3.grid(row=2, column=1)
        self.btn2 = exit_widget(self)
        self.btn2.grid(row=2, column=2)

    def get_and_change_time(self, input_class):
        """Gets and changes the time on the label with the given tkinter class of input. """
        inp = input_class()
        logger.debug('Input with class %s started' % input_class.__name__)
        inp.mainloop()
        logger.debug('Finished mainloop.')
        logger.debug('Seconds: %s', inp.secs)
        logger.debug('Formatted string: %s', inp.format_string)
        self.lbl.config(text='%d Seconds' % inp.secs)
        logger.debug('Configed? first label')
        self.lbl2.config(text=inp.format_string)
        logger.debug('Configed? second label')