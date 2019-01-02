from abc import ABCMeta, abstractmethod
from datetime import datetime
from tkinter import Tk

from Countdown import create_logger
from .SmartKinter import SmartLabel, SmartButton, SmartEntry
from .error_boxes import ErrorAndMsg
from .prefab import exit_widget

logger = create_logger('Input Windows')


class InputBase(Tk, metaclass=ABCMeta):
    def __init__(self):
        """Initializes the class and creates the two buttons."""
        super().__init__()
        self.labelinputdict = {}
        self.entered_values = []
        self.rnum = 1
        self.btn3 = exit_widget(self)
        self.btn1 = SmartButton(self, text='Set Time', command=self.get_all_data)
        self.secs = 0

    def build_label_input(self, value='', row=0, text='', largs=None, fargs=None, lgridargs=None, fgridargs=None):
        """Builds the label and the input field for it."""
        if lgridargs is None:
            lgridargs = {'column': 0}
        if fgridargs is None:
            fgridargs = {'column': 1, 'columnspan': 2}
        if largs is None:
            largs = {}
        if fargs is None:
            fargs = {}
        lbl = SmartLabel(self, text=text, font_size=12, **largs)
        lbl.grid(row=row, **lgridargs)
        fld = SmartEntry(self, **fargs)
        fld.grid(row=row, **fgridargs)
        fld.insert(0, value)
        self.labelinputdict[lbl] = fld

    def build_window(self):
        """Builds the window."""
        self.label1.grid(row=0, column=0, columnspan=3)
        self.build_iterable()
        self.btn1.grid(row=self.rnum, columnspan=2)
        self.btn3.grid(row=self.rnum, column=2)

    @abstractmethod
    def build_iterable(self):
        """Builds the window from a list or dictionary"""

    @abstractmethod
    def get_all_data(self):
        """Gets all of the values, and convers them to seconds."""

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

    def finish(self):
        """Does seconds_to_hr_min_sec, quits and destroys."""
        self.seconds_to_hr_min_sec()
        self.quit()
        self.destroy()


class TimeInput(InputBase):
    """Builds the window to input time."""

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.vals = ['Hours', 'Minutes', 'Seconds']
        self.rvals = [60 * 60, 60, 1]
        self.label1 = SmartLabel(self, text='Input the time.')
        self.build_window()
        self.secs = self.seconds = self.minutes = self.hours = 0
        self.format_string = ''

    def build_iterable(self):
        for i in self.vals:
            self.build_label_input(row=self.rnum, text=i, value='0')
            self.rnum += 1

    def get_all_data(self):
        """Gets all of the entered values and converts them into seconds."""
        self.secs = 0
        for i in range(len(self.rvals)):
            dv = self.labelinputdict[list(self.labelinputdict)[i]].get()
            logger.debug('Amount: %s, Value: %s, Total: %s', dv, self.rvals[i], self.rvals[i] * int(dv))
            self.secs += self.rvals[i] * int(dv)
            logger.debug('Seconds: %d', self.secs)
        self.finish()


class DateInput(InputBase):
    """A class to input a date to count down to."""

    def __init__(self):
        """Initalizes the class"""
        super().__init__()
        self.lbls = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']
        self.label1 = SmartLabel(self, text='Input the date.')
        self.build_window()

    @staticmethod
    def get_formatted_date():
        return datetime.now().strftime('%Y-%m-%d-%H-%M-%S').split('-')

    def build_iterable(self):
        for a, b in dict(zip(self.lbls, self.get_formatted_date())).items():
            self.build_label_input(value=b, row=self.rnum, text=a)
            self.rnum += 1

    def get_all_data(self):
        s = ''
        for a, b in self.labelinputdict.items():
            s += b.get()
        dt = datetime.strptime(s, '%Y%m%d%H%M%S')
        diff = (dt - datetime.now())
        logger.debug('DT: %s\nCurrent: %s\nTD: %s\nSeconds: %d' % (dt, datetime.now(), diff, diff.seconds))
        if diff.days < 0:
            ErrorAndMsg('Date already happened!').mainloop()
            self.secs = 0
            self.finish()
            self.quit()
            self.destroy()
        else:
            self.secs = diff.seconds
            self.finish()
