from datetime import datetime
from tkinter import Tk

from .SmartKinter import SmartLabel, SmartButton, SmartEntry
from .consts import second, minute, hour, day, week, month, year
from .error import TooLittleTimeError, TooMuchTimeError


class TimeCalculator(object):
    """A class to retrieve the differences based on the amount of seconds in it."""

    def __init__(self, seconds: int):
        """Initializes the class

        :param seconds: The amount of seconds to process
        :type seconds: int
        """
        self.run_main(seconds)

    def run_main(self, seconds: int):
        """The same thing as init, code from init to here in order to allow class inheritance."""
        self.timedict = {'sec': seconds}
        self.seconds = seconds
        if seconds < second:
            raise TooLittleTimeError(seconds)
        elif not isinstance(seconds, int):
            raise ValueError('Seconds needs to be int, not %s' % seconds.__class__.__name__)
        elif minute < seconds < hour:
            self.min_sec()
        elif hour < seconds < day:
            self.hr_min_sec()
        elif day < seconds < week:
            self.dy_hr_min_sec()
        elif week < seconds < month:
            self.wk_dy_hr_min_sec()
        elif month < seconds < year:
            self.mn_wk_dy_hr_min_sec()
        elif year < seconds < year * (2100 - datetime.now().year):
            self.yr_mn_wk_dy_hr_min_sec()
        elif seconds > year * (2100 - datetime.now().year):
            raise TooMuchTimeError(seconds)
        else:
            raise ValueError(
                'Seconds is not a normal integer, is %s with value %s' % (seconds.__class__.__name__, seconds))
        self.clean_dict()
        self.dict_to_word()

    def min_sec(self):
        self.timedict['min'], self.timedict['sec'] = divmod(self.seconds, minute)

    def hr_min_sec(self):
        self.min_sec()
        self.timedict['hr'], self.timedict['min'] = divmod(self.timedict['min'], hour)

    def dy_hr_min_sec(self):
        self.hr_min_sec()
        self.timedict['dy'], self.timedict['hr'] = divmod(self.timedict['hr'], day)

    def wk_dy_hr_min_sec(self):
        self.dy_hr_min_sec()
        self.timedict['wk'], self.timedict['dy'] = divmod(self.timedict['dy'], week)

    def mn_wk_dy_hr_min_sec(self):
        self.wk_dy_hr_min_sec()
        self.timedict['mn'], self.timedict['wk'] = divmod(self.timedict['wk'], month)

    def yr_mn_wk_dy_hr_min_sec(self):
        self.mn_wk_dy_hr_min_sec()
        self.timedict['yr'], self.timedict['mn'] = divmod(self.timedict['mn'], year)

    def clean_dict(self):
        kvpairs = [(key, item) for key, item in self.timedict.items()]
        for k, i in kvpairs:
            if i == 0:
                del self.timedict[k]

    def dict_to_word(self):
        self.wordstr = ''
        for a, b in self.timedict.items():
            self.wordstr += '%d %s' % (b, a)


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
            self.secs += self.rvals[i] * int(dv)
        self.destroy()
