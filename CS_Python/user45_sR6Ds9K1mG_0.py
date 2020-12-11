# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

range_g = 100
n=7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=random.randrange(0,range_g)    
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_g,n
    n=7
    range_g = 100
    print(" You are playing in range [0,100)")
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_g,n
    n=10
    range_g = 1000
    print(" You are playing in range [0,1000)")
    new_game()
    
    
def input_guess(t):
    # main game logic goes here	
    global guess, secret_number,n
    guess= int(t)
    
    n=n-1
    if n>0:
        print( "Number of guesses left: " + str(n))
    elif n==0:
        print("You lost,try again")
        new_game()
        
    print("Your guess is: " + t)
    
    if guess > secret_number:
        print("Lower")
    elif guess < secret_number:
        print("Higher")
    elif guess==secret_number:
        print("Correct!")
       
    
    

    
    

    
# create frame

frame  = simplegui.create_frame  ("Guess the number", 100,300)


# register event handlers for control elements and start frame
button1= frame.add_button("Range [0,100)",range100,100)
button2= frame.add_button("Range [0,1000)", range1000,100)
inp=frame.add_input("Enter your guess",input_guess,100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
