"""
UNFINISHED CODE
"""

from breezypythongui import EasyFrame, EasyDialog


#class WinnerDialog(EasyDialog):

    #def __init__(self, parent):
        #EasyDialog.__init__(self, parent, "Game Over")

class NumberGuessGUI(EasyFrame):

    def __init__(self, model):
        EasyFrame.__init__(self, title = "Number Guessing Game")

        self.addLabel(text = "My Guess", row = 0, column = 0)
        self.addButton(text = "Correct", row=1, column=0, command = self.correct)

        self.addButton(text = "Too Low", row=1, column=1, command = self.low)

        self.addButton(text = "Too High", row=1, column=2, command = self.high)
        #self.popup = WinnerDialog(self)
        self.model = model

        self.count =1

    def low(self):
        self.count+=1

    def high(self):
        self.count+=1

    def correct(self):
        #WinnerDialog(self)
        self.messageBox("Game Over", "My guess is % for % guesses" % (self.model.guess(), 99)
        
    
