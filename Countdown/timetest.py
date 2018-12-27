from tkinter import Tk

from .SmartKinter import SmartLabel, SmartButton
from .input_windows import TimeCalculator, TimeInput


class TimeTest(Tk):
    def __init__(self):
        super().__init__()
        self.sec = 0
        self.lbl = SmartLabel(self, text='0 Seconds')
        self.lbl2 = SmartLabel(self, text='0 Seconds')
        self.lbl.grid(columnspan=2)
        self.lbl.grid(columnspan=2)
        self.btn1 = SmartButton(self, text='Input And Change Time', command=self.get_and_change_time)
        self.btn1.grid(row=1)
        self.btn2 = SmartButton(self, text='Quit', command=self.destroy)
        self.btn2.grid(row=1, column=1)

    def get_and_retrieve_time(self):
        inp = TimeInput()
        inp.mainloop()
        self.TC = TimeCalculator(inp.seconds)

    def get_and_change_time(self):
        self.get_and_retrieve_time()
        self.lbl.configure(text='%d Seconds' % self.TC.seconds)
        self.lbl2.configure(text=self.TC.wordstr)
