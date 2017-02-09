# Sorting Hat - variation on the magic 8-ball.
# Shaking makes the hat think for a while before
# finding which Hogwarts house you belong in.

from microbit import *
import random

# Images for the sorting hat and the four hogwarts houses
hat = Image(
            "07900:"
            "60750:"
            "07070:"
            "09090:"
            "99999")

# Snake            
slytherin = Image(
            "09999:"
            "90099:"
            "09940:"
            "40090:"
            "09940")
 
# Badger 
hufflepuff = Image(
            "99999:"
            "90909:"
            "90909:"
            "09090:"
            "00900") 

# Claw
ravenclaw = Image(
            "00900:"
            "00900:"
            "09990:"
            "90909:"
            "90909")

# Sword
gryffindor = Image(
            "00009:"
            "00090:"
            "90900:"
            "09000:"
            "90900")
            
choices = [

    ["Slytherin", slytherin],
    ["Hufflepuff", hufflepuff],
    ["Ravenclaw", ravenclaw],
    ["Gryffindor", gryffindor]
]

thinking = [

    "Hmm. Difficult",
    "Very Difficult...",
    "So where shall I put you?",
    "Ah, right then",
    "Hmm, right",
    "Hmm",
    "Okay",
    "Well, I know just what to do with you...",
    "Right, Ok",
    "Not Slytherin, Eh?"
]


# Game loop
while True:

    display.show(hat)

    if accelerometer.was_gesture("shake"):
        display.clear()
        display.scroll(random.choice(thinking))
        sleep(1000)
        
        house = random.choice(choices)
        
        # House name...
        display.scroll(house[0])
        # House picture
        display.show(house[1])
        sleep(2000)
        