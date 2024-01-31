# 1. Importing the Required Libraries for Python Number Guessing Game

import tkinter as tk    # Tkinter Module – help us with the creation of a GUI window
from tkinter import *
import random           # Random Module – We will be using this module to generate a random number that the user will be guessing.


# 2. Creating the GUI Window:

win = tk.Tk()           # Using the TK() we make a window named win.
win.geometry("750x550") #  specify the size of the window using the geometry() function
win.title("Guess The Number Game")  # give a title to it using the title() function

# 4. Create The Main Function – Execution of the game:

hint = StringVar()      # Hint- For displaying the hints. Using the StringVar() method we have specified that it is of string type.
score = IntVar()        # Score – For displaying the score initially. Using the IntVar() method we have specified that it is of integer type.
final_score= IntVar()   # Final_score – For displaying the updated score after every round or every guess. Using the IntVar() method we have specified that it is of integer type.
guess= IntVar()         # Guess – This stores the number that the user has entered.

num=random.randint(1,50) # Randint() – this function is to randomly generate a number in the specified range

''' Using the set() method we set what will be the value of these variables when they are displayed on the window. '''
hint.set("Guess a number between 1 to 50 ")
score.set(5)
final_score.set(score.get())

''' We have created a function fun() to compare the number entered to the generated number and then after comparing make the necessary changes on the display window. '''
def fun():
    x=guess.get()       # We have extracted the entered number using the get() method and saved its value in a variable x.
    final_score.set(score.get())
    
    if score.get()>0:   # Using the if-else loops in python, we check if the number is equal to the generated number, less than, greater 
                        # than or not in the range. According to these conditions we update the score and hints. Everytime a guess goes 
        if x > 20 or x<0: # wrong the final score becomes one less so there are a total of 5 chances.
            hint.set("You just lost 1 Chance")
            score.set(score.get()-1)
            final_score.set(score.get())
    
        elif num==x:
            hint.set("Congratulation YOU WON!!!") # If the user guesses the right number, a congratulatory message is displayed. 
            score.set(score.get()-1)
            final_score.set(score.get())
      
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            score.set(score.get()-1)
            final_score.set(score.get())
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            score.set(score.get()-1)
            final_score.set(score.get())
    else:
         hint.set("Game Over You Lost") # If a user loses all chances then a sorry message is displayed. We set the value of these variables as given in the conditions using the set() method.

# 3. Creating the Labels, Entry Boxes and Button:

'''we have created an entry field using the Entry() function where we specify the width of the entry field, font, size of the text etc. 
To place this entry field, we make use of the place() function. In the place() function, we specify the x-y coordinates and also the anchor 
as center. There are a total of 3 Entry fields that we have created. '''

# 1. Entry area to enter a number:
Entry(win, textvariable=guess, width=3,font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

# 2. Displaying the current score:
Entry(win, textvariable=hint, width=50,font=('Courier', 15), relief=GROOVE,bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)

# 3. Displaying the hints:
Entry(win, text=final_score, width=2,font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

''' We have created labels using the Label() function. These labels are primarily to display a text.To place this label, we make use of 
the place() function. In the place() function, we specify the x-y coordinates and also the anchor as center. '''

Label(win, text='I challange you to guess the number ',font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)

Label(win, text='Score out of 5',font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

''' We create a Check Button which will check if the user’s number is equal to the number generated through the random module. command=fun 
will initiate the fun function which will generate hints and perform the comparison between the generated number and the number entered by 
the user. '''

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE,bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()

'''
Summary
We have successfully created the Number Guessing Game with the help of Tkinter Module and Random Module of Python. 
We learned about these modules and their inbuilt functions during the project.
'''