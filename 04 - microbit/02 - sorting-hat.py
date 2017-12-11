# Sorting Hat - variation on the magic 8-ball.
# Shaking makes the hat think for a while before
# finding which Hogwarts house you belong in.

from microbit import *
import random
import speech

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

    ["Slither in", slytherin],
    ["Huffle puff", hufflepuff],
    ["Ray ven claw", ravenclaw],
    ["Griff in door", gryffindor]
]

thinking = [

    "Difficult",
    "Very Difficult...",
    "So where shall I put you?",
    "Ah, right then",
    "Hmm, right",
    #"Hmm",
    "Okay",
    "Well, I know just what to do with you...",
    "Right, Okay",
    "Not Slither in, Eh?"
]

speech.say("David!")
sleep(1000)
speech.say("Go to bed")
sleep(1000)
speech.say("you spenk")
sleep(100000)

voice_speed = 80
voice_pitch = 100
voice_throat = 100
voice_mouth = 100

# Game loop
while True:

    display.show(hat)

    if True: #accelerometer.was_gesture("shake"):
        display.clear()
        speech.say("you are a wizard harry!", speed = voice_speed, pitch = voice_pitch, throat = voice_throat, mouth = voice_mouth)
        sleep(1000)
        thought = random.choice(thinking)
        speech.say(thought, speed = voice_speed, pitch = voice_pitch, throat = voice_throat, mouth = voice_mouth)
        #display.scroll(random.choice(thinking))
        sleep(1000)
        
        house = random.choice(choices)
        
        # House name...
        speech.say(house[0], speed = voice_speed, pitch = voice_pitch, throat = voice_throat, mouth = voice_mouth)
        #display.scroll(house[0])
        # House picture
        display.show(house[1])
        sleep(2000)
        