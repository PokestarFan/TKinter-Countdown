from tkinter import Tk

from .SmartKinter import SmartLabel
from .prefab import exit_widget


class ErrorAndMsg(Tk):
    def __init__(self, text=""):
        super().__init__()
        self.lbl1 = SmartLabel(self, font_size=72, text='Error!')
        self.lbl2 = SmartLabel(self, text=text)
        self.btn1 = exit_widget(self, text='OK')
        self.btn2 = exit_widget(self, text='Cancel')
        self.build_window()

    def build_window(self):
        self.lbl1.grid(rowspan=2, columnspan=2)
        self.lbl2.grid(row=2, columnspan=2)
        self.btn1.grid(row=3)
        self.btn2.grid(row=3, column=1)

    def destroy(self, quitted=False):
        super().quit()
        super().destroy()
