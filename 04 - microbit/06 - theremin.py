from microbit import *

import music

frequency = 440 # concert a
sprite = [2, 2]

while True:

    display.clear()
    display.set_pixel(sprite[0], sprite[1], 9)

    x = accelerometer.get_x() / 512
    y = accelerometer.get_y() / 512
    x = abs(x + 2)
    y = abs(y + 2)
    sprite[0] = x
    sprite[1] = y

    x_offset = x * 100
    y_offset = y * 500
    offset = x_offset + y_offset
    music.pitch(440 + offset) # a + 
    sleep(100)
