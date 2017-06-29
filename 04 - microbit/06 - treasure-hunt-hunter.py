# Treasure Hunt Clue Receiver
from microbit import *
import radio

# starting clue
clue = "Walk around to find the first clue"
next_clue = 0

radio.on()

while True:

    radio.send(str(next_clue))

    # are we near any clue beacons?
    message = radio.receive()

    if message:
        # we have a new clue !
        clue = message
        display.scroll(clue)
        next_clue += 1

    # press a button to show the last clue
    if button_a.was_pressed() or button_b.was_pressed():
        display.scroll(clue)

    sleep(500)

    # extension use buttons to go back and forward looking for numbered clues?
