# Treasure Hunt Clue Beacon
from microbit import *
import radio

# Pirates !!!
skull = Image("09990:90909:99099:99999:04440")
cross_bones = Image("94009:49090:00900:09094:90049")
skull_and_cross_bones = [skull, cross_bones]
display.show(skull_and_cross_bones)

all_clues = [
    "Walk Fifteen paces east",
    "Ten paces north",
    "Walk forwards",
    "Look under the seat",
    "Hooray, you win!"
]

clue_count = len(all_clues)

# the clue this unit will broadcast
# can be changed by the a and b buttons
clue = 1

radio.on()

beacon_off = Image("00000:00000:00900:09090:99999")
beacon_on  = Image("00000:00900:00900:09090:99999")
beacon_animation = [beacon_off, beacon_on, beacon_off]

while True:
    
    # show which clue we are broadcasting
    display.show(beacon_animation)

    # decrease clue number
    if button_a.was_pressed():
        clue = max(clue - 1, 1)
        display.show(str(clue))
    # increase clue number
    elif button_b.was_pressed():
        clue = min(clue +  1, clue_count)
        display.show(str(clue))
    # broadcast the current clue
    else:
        clue_text = str(clue) + ":" + all_clues[clue - 1]
        radio.send(clue_text)
                
    sleep(1000)
        
        
