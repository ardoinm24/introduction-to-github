"""
UNFINISHED CODE
"""

class NumberGuess():

    def __init__(self, low = 1, high = 100):
        self.low = low
        self.high = high
    
    def guess(self):
        return (self.low + self.high -1)/2

    def tooHigh(self):
        self.high = self.guess()

    def tooLow(self):
        self.low = self.guess()

    def correct(self):
        "You win!"

def main():

    game = NumberGuess()

    
    if len(sys.argv) == 3:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
    print("Good morning, welcome to the game of guess the number!")
    print("Choose a number between 1 and 100!" % (low, high))
    #number = random.randint(low, high)
    count = 0
    while True:
        count += 1
        print("My guess is", guess(self), "for", count, "guess(es)!")
        if answer == 'H':
            game.tooHigh()
        elif answer == 'L':
            game.tooLow()
        elif anwser == 'C':
            game.correct()
        #guess = int(input('Enter your guess: '))
        #if guess == number:
            #print("You got it in %d tries!" % count)
            #break
        #elif guess < number:
            #print("Sorry, too low!")
        #else:
            #print("Sorry, too high!")
        #if count > (math.log2(low + high -1)):
            #print("Too many guesses! You lose!")
            #break
    print("Have a nice day!")
