# Treasure Hunt Clue Beacon
from microbit import *

# Starting image
skull = Image("09990:90909:99099:99999:04440")
cross_bones = Image("94009:49090:00900:09094:90049")
skull_and_cross_bones = [skull, cross_bones]

display.show(skull_and_cross_bones)

all_clues = [
    "Fifteen paces east",
    "Ten paces north",
    "Walk forwards",
    "Look under the seat",
    "hooray, you win!"
]

clue_count = len(all_clues)

# the clue this unit will broadcast
# can be changed by the a and b buttons
clue = 0

radio.on()

while True:
    # show which clue we are broadcasting
    display.scroll(str(clue))

    # decrease clue number
    if button_a.was_pressed():
        clue -= 1
        if clue < 0:
            clue = clue_count - 1
    # increase clue number
    elif button_b.was_pressed():
        clue += 1
        if clue >= clue_count:
            clue = 0
    # check for incoming message
    else:
        message = radio.receive()

        if message:
            # expecting a clue number
            requested_clue = int(message)

            if clue == requested_clue:
                radio.send(all_clues[clue])

        sleep(500)
