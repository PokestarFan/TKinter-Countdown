from tkinter import Tk

from Countdown import create_logger
from .SmartKinter import SmartLabel, SmartButton, SmartEntry
from .consts import second, minute, hour, day, week, month, year

logger = create_logger('Input Windows')


class TimeInput(Tk):
    """Builds the window to input time."""

    def __init__(self):
        super().__init__()
        self.labelinputdict = {}
        self.rnum = 1
        self.btn3 = SmartButton(self, text='Quit', command=self.destroy)
        self.btn1 = SmartButton(self, text='Get Seconds and Quit', command=self.get_all_entered_vals)
        self.vals = ['Years', 'Months', 'Weeks', 'Days', 'Hours', 'Minutes', 'Seconds']
        self.rvals = [year, month, week, day, hour, minute, second]
        self.label1 = SmartLabel(self, text='Input the time.')
        self.build_window()
        self.secs = 0

    def build_window(self):
        """Builds the window."""
        self.label1.grid(row=0, column=0, columnspan=3)
        for i in self.vals:
            self.build_label_input(row=self.rnum, text=i, largs={'font_size': 12})
            self.rnum += 1
        self.btn1.grid(row=self.rnum, columnspan=2)
        self.btn3.grid(row=self.rnum, column=2)

    def build_label_input(self, row=0, text='', largs=None, fargs=None, lgridargs=None, fgridargs=None):
        """Builds the label and the input field for it."""
        if lgridargs is None:
            lgridargs = {'column': 0}
        if fgridargs is None:
            fgridargs = {'column': 1, 'columnspan': 2}
        if largs is None:
            largs = {}
        if fargs is None:
            fargs = {}
        lbl = SmartLabel(self, text=text, **largs)
        lbl.grid(row=row, **lgridargs)
        fld = SmartEntry(self, **fargs)
        fld.grid(row=row, **fgridargs)
        fld.insert(0, '0')
        self.labelinputdict[lbl] = fld

    def get_all_entered_vals(self):
        self.secs = 0
        for i in range(len(self.rvals)):
            dv = self.labelinputdict[list(self.labelinputdict)[i]].get()
            logger.debug('Amount: %s, Value: %s, Total: %s', dv, self.rvals[i], self.rvals[i] * int(dv))
            self.secs += self.rvals[i] * int(dv)
            logger.debug('Seconds: %d', self.secs)
        self.quit()
        self.destroy()
