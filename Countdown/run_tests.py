import sys
from os import getcwd, chdir, mkdir
from os.path import isdir
from tkinter import Label, Button, Tk, LEFT
from typing import Callable

from Countdown import create_logger
from Countdown.SmartKinterTest import SmartKinterTest
from Countdown.timetest import TimeTest

logger = create_logger('Main')


def wipe_file():
    """Wipes the file that is used to control the log file name."""
    if getcwd().split('\\')[-1] == 'Countdown':
        chdir('..')
        if not isdir('logs'):
            mkdir('logs')
        chdir('logs')
    open('created.txt', 'w').close()


# noinspection PyBroadException
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
        self.call('wm', 'attributes', '.', '-topmost', True)
        logger.info('Tester class started')

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
        """Runs a function and prints that it was run. Parameters are the same as gen_test_button."""

        def temp():
            logger.info('Running function %s', name)
            try:
                callback()
            except Exception:
                logger.exception('Running function %s failed.', name)

        return temp

    def destroy(self, quitted=False):
        """Destroys the window and exits the process"""
        if not quitted:
            self.quit()
        else:
            super().destroy()
            wipe_file()
            logger.info('Program exiting')
            sys.exit(0)

    def quit(self):
        """Quits mainloop. Linked to destroy."""
        super().quit()
        self.destroy(quitted=True)


tester = Tester()
tester.gen_test_button(lambda: SmartKinterTest().mainloop(), 'SmartKinterTest')
tester.gen_test_button(lambda: TimeTest().mainloop(), 'TimeTest')
tester.mainloop()
