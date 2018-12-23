import calendar
import sys
import tkinter as Tkinter
import tkinter.ttk as ttk

from ._calendar import Calendar


class Test(Tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ttk Calendar')
        ttkcal = Calendar(firstweekday=calendar.SUNDAY)
        ttkcal.pack(expand=1, fill='both')
        if 'win' not in sys.platform:
            style = ttk.Style()
            style.theme_use('clam')


if __name__ == '__main__':
    Test().mainloop()
