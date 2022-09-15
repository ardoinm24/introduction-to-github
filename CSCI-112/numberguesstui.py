"""
Mary Ardoin
Project 1
File: numberguesstui.py
"""

import random
import sys
import math

def main(low = 1, high = 20):
    """Default range is 1..100."""
    if len(sys.argv) == 3:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
    print("Good morning, welcome to the game of guess the number!")
    print("I am thinking of a number between %d and %d." % (low, high))
    number = random.randint(low, high)
    count = 0
    while True:
        count += 1
        guess = int(input('Enter your guess: '))
        if guess == number:
            print("You got it in %d tries!" % count)
            break
        elif guess < number:
            print("Sorry, too low!")
        else:
            print("Sorry, too high!")
        if count > (math.log2(low + high -1)):
            print("Too many guesses! You lose!")
            break
    print("Have a nice day!")
    
    
        

if __name__ == "__main__":
    main()
           
            
    

    
        
    



    
    
    

