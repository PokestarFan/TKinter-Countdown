import sys
from tkinter import Label, Button, Tk, LEFT
from typing import Callable

from Countdown.SmartKinterTest import SmartKinterTest
from Countdown.timetest import TimeTest


class Tester(Tk):
    """A class to make the window of the tester."""

    def __init__(self):
        """Initializes the class. Also creates the other buttons"""
        super().__init__()
        self.label = (Label(self, text='Run Test Commands', font=('Courier New', 36)))
        self.label.pack()
        self.end_button = Button(self, text='Quit', font=('Courier New', 12), command=self.destroy)
        self.end_button.pack(side=LEFT)
        self.buttons = []
        print('Tester class started')

    def gen_test_button(self, callback: Callable, name: str) -> None:
        """
        Generates a button for a callback function, usually a Test function.

        :param callback: The function to be run
        :param name: The name of the thing being tested
        :type callback: Callable
        :type name: str
        :return: None
        :rtype: None
        """
        self.buttons.append(Button(self, text=name, font=('Courier New', 12), command=self.run_cb(callback, name)))
        self.buttons[-1].pack(side=LEFT)

    @staticmethod
    def run_cb(callback: Callable, name: str):
        """Runs a function and prints that it was run. Parameters are the same as gen_test_button.

        :param callback: The function to be run
        :param name: The name of the thing being tested
        :type callback: Callable
        :type name: str
        :return: None
        :rtype: None
        """

        def temp():
            print('Running function %s' % name)
            callback()

        return temp

    def destroy(self):
        """Destroys the window and exits the process"""
        super().destroy()
        sys.exit(0)

    def quit(self):
        """Linked to destroy."""
        self.destroy()


tester = Tester()
tester.gen_test_button(lambda: SmartKinterTest().mainloop(), 'SmartKinterTest')
tester.gen_test_button(lambda: TimeTest().mainloop(), 'TimeTest')
tester.mainloop()
