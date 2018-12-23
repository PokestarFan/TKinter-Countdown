"""This is the Test module for smartkinter."""

from tkinter import Tk

from .SmartKinter import SmartButton, SmartLabel


class SmartKinterTest(Tk):
    def __init__(self):
        super().__init__()
        self.label = SmartLabel(self, text='Test')
        self.label2 = SmartLabel(self, text='Test 2')
        self.label.grid(row=0, columnspan=2)
        self.label2.grid(row=1, columnspan=2)
        self.btn1 = SmartButton(self, text='Run Test', command=self.test_run)
        self.btn2 = SmartButton(self, text='Stop', command=self.destroy)
        self.btn1.grid(row=2, column=1)
        self.btn2.grid(row=2)

    def test_run(self):
        self.label.config(text='It worked!')
        self.label2.config(text='It also worked!')
