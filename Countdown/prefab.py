"""This module defnes commonly used buttons"""
from .SmartKinter import SmartButton


def exit_widget(widget, text='Quit'):
    return SmartButton(widget, text=text, command=widget.destroy)
