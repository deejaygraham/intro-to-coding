# micro:bit emotion

# Communicate your emotion to another microbit

import radio
import random
from microbit import *

# name image pairs
emotions = [

    ['happy', Image.HAPPY],
    ['sleepy', Image.ASLEEP],
    ['sad', Image.SAD],
    ['surprised', Image.SURPRISED],
    ['confused', Image.CONFUSED],
    ['meh', Image.MEH],
    ['duck', Image.DUCK]
]

emotion_count = len(emotions)

current_emotion = 0

square1 = Image(
            "00000:"
            "00000:"
            "00000:"
            "00000:"
            "90000")

square2 = Image(
            "00000:"
            "00000:"
            "00000:"
            "99000:"
            "09000")

square3 = Image(
            "00000:"
            "00000:"
            "99900:"
            "00900:"
            "00900")

square4 = Image(
            "00000:"
            "99990:"
            "00090:"
            "00090:"
            "00090")

square5 = Image(
            "99999:"
            "00009:"
            "00009:"
            "00009:"
            "00009")


incoming_msg = [square1, square2, square3, square4, square5]

radio.on()
display.clear()

simulate_msg = 0

while True:

    display.show(emotions[current_emotion][1])
    
    # select an emotion
    if button_a.was_pressed():
        current_emotion += 1
        if current_emotion >= emotion_count:
            current_emotion = 0
            
    # send that emotion
    elif button_b.was_pressed():
        radio.send(emotions[current_emotion][0])
        simulate_msg = 1
        
    # Read any incoming messages.
    message = radio.receive()
    
    if simulate_msg == 1:
        message = random.choice(emotions)[0]
        simulate_msg = 0
        
    find_emotion = 0
    for emotion in emotions:
        if message == emotion[0]:
            current_emotion = find_emotion
            display.show(incoming_msg, delay=50)
            display.clear()
            sleep(100)
        find_emotion += 1        
         
