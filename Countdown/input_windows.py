from tkinter import Tk

from Countdown import create_logger
from .SmartKinter import SmartLabel, SmartButton, SmartEntry

logger = create_logger('Input Windows')


class TimeInput(Tk):
    """Builds the window to input time."""

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.labelinputdict = {}
        self.rnum = 1
        self.btn3 = SmartButton(self, text='Quit', command=self.destroy)
        self.btn1 = SmartButton(self, text='Get Seconds and Quit', command=self.get_all_entered_vals)
        self.vals = ['Hours', 'Minutes', 'Seconds']
        self.rvals = [60 * 60, 60, 1]
        self.label1 = SmartLabel(self, text='Input the time.')
        self.build_window()
        self.secs = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.format_string = ''

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
        """Gets all of the entered values and converts them into seconds."""
        self.secs = 0
        for i in range(len(self.rvals)):
            dv = self.labelinputdict[list(self.labelinputdict)[i]].get()
            logger.debug('Amount: %s, Value: %s, Total: %s', dv, self.rvals[i], self.rvals[i] * int(dv))
            self.secs += self.rvals[i] * int(dv)
            logger.debug('Seconds: %d', self.secs)
        self.seconds_to_hr_min_sec()
        self.quit()
        self.destroy()

    @staticmethod
    def check_for_both(var):
        """Checks to see if the number is 0 or a single digit number. If the number is zero than another zero is added.
        If the number is a single digit number, a zero is added to the front of it."""
        if var == 0:
            return '%d0:' % var
        elif 0 < var < 10:
            return '0%d:' % var
        else:
            return '%d:' % var

    def check_and_add(self, var):
        """Runs the check function and adds them to the format_string attribute of the class."""
        self.format_string += self.check_for_both(var)

    def add_hr_min_sec(self):
        """Runs check and add on the hours, minutes and seconds attributes. It also deletes the last character of the
        string if the last character is a colon."""
        self.format_string = ''
        self.check_and_add(self.hours)
        self.check_and_add(self.minutes)
        self.check_and_add(self.seconds)
        if self.format_string[-1] == ':':
            self.format_string = self.format_string[:-1]

    def seconds_to_hr_min_sec(self):
        """Converts the seconds from the input into seconds, minutes and hours. Also formats them into a string using
        the add_hr_min_sec function."""
        self.minutes, self.seconds = divmod(self.secs, 60)
        self.hours, self.minutes = divmod(self.minutes, 60)
        self.add_hr_min_sec()
