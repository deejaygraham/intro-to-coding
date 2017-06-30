# Treasure Hunt Clue Receiver
from microbit import *
import radio

# Pirates !!!
skull = Image("09990:90909:99099:99999:04440")
cross_bones = Image("94009:49090:00900:09094:90049")
skull_and_cross_bones = [skull, cross_bones]
display.show(skull_and_cross_bones)

# starting clue
clue = "hint: Walk around to find the first clue"
display.scroll(clue)

next_clue = 1

radio.on()

while True:

    display.show("?")
    
    # are we near any clue beacons?
    message = radio.receive()

    if message:
        # picked up a clue !
        number, text = message.split(":")
        # is it the one we want?
        if int(number) == next_clue:
            clue = "clue " + str(number) + ":" + text
            next_clue += 1
            display.scroll(clue)

    # press a button to be reminded about the last clue
    if button_a.was_pressed() or button_b.was_pressed():
        display.scroll(clue)

    sleep(100)

    # extension use buttons to go back and forward looking for numbered clues?
