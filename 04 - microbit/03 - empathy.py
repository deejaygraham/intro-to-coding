# micro:bit empathy.
import radio
import random
from microbit import *

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

while True:

    display.show(centre_cube)

    # Shake to send a message
    if accelerometer.was_gesture("shake"):
        radio.send('shake')
        sleep(5000)
        for i in range(1, 5):
            display.show(shake_frames) #, delay=200, wait=False)
        sleep(200)


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
