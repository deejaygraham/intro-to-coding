# micro:bit empathy

# Displays a static block in centre of display.
# When shaken, uses radio to send a message
# to surrounding microbits. Any microbit receiving
# the message will shake their own block for a
# few seconds

import radio
import random
from microbit import *

#emotions = [Image.HAPPY, Image.ASLEEP, Image.SAD, Image.SURPRISED, Image.CONFUSED, Image.MEH, Image.DUCK]

#current_emotion = 0


centre_cube = Image(
            "00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000")

left_cube = Image(
            "00000:"
            "99900:"
            "99900:"
            "99900:"
            "00000")

right_cube = Image(
            "00000:"
            "00999:"
            "00999:"
            "00999:"
            "00000")

shake_frames = [centre_cube, left_cube, centre_cube, right_cube]

radio.on()
display.clear()

while True:

    display.show(emotions[current_emotion])

    # select an emotion
    if button_a.was_pressed():

    # send that emotion
    elif button_b.was_pressed():
        radio.send('')

#    display.show(centre_cube)

    # Shake to send a message
#    if accelerometer.was_gesture("shake"):
#        radio.send('shake')
#        sleep(5000)
#        for i in range(1, 5):
#            display.show(shake_frames) #, delay=200, wait=False)
#        sleep(200)


    # Shake to send a message
#    if accelerometer.was_gesture("shake"):
#        radio.send('shake')

    # Read any incoming messages.
#    incoming = radio.receive()
#    if incoming == 'shake':
#        sleep(200)
#        for i in range(1, 5):
#            display.show(shake_frames) #, delay=200, wait=False)
#        sleep(200)

# press button a to find your emotion. Send that using button b
# anyone can receive that emotion.
