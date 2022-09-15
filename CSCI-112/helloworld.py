"""
Mary Ardoin
Project 1
File: helloworld.py

"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class HelloWorld(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.addLabel(text = "Hello world!", row = 0, column = 0, sticky = "NSEW",
                      font = Font(size=24, weight = 'bold'), foreground = 'red')

def main():
    """The starting point for launching the program."""
    HelloWorld().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
