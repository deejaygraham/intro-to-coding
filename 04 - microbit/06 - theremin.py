from microbit import *

import music

frequency = 440 # concert a

while True:

    display.clear()
    display.set_pixel(sprite[0], sprite[1], 9)

    x = accelerometer.get_x() / 512
    y = accelerometer.get_y() / 512
    x = abs(x + 2)
    y = abs(y + 2)
    sprite[0] = x
    sprite[1] = y

    # alternative
    up_down = accelerometer.get_y() / 20
    side_to_side = accelerometer.get_x() / 20
    back_forwards = accelerometer.get_z() / 20
    change = up_down + side_to_side + back_forwards
    # music.pitch(440 + change) # a +

    x_offset = x * 100
    y_offset = y * 500
    offset = x_offset + y_offset
    
    music.pitch(440 + int(offset)) # a +
    sleep(100)

    # extend to use notes from a scale 
