# Die/dice game

from microbit import *
import random

# use dice images ?

while True:

    if accelerometer.was_gesture("shake"):
        die_value = random.randint(1, 6)
        display.clear()
        sleep(300)
        # display.show(str(die_value))            
        
        if die_value == 1:
            display.set_pixel(2, 2, 9)
        elif die_value == 2:
            display.set_pixel(0, 0, 9)
            display.set_pixel(4, 4, 9)
        elif die_value == 3:
            display.set_pixel(0, 0, 9)
            display.set_pixel(2, 2, 9)
            display.set_pixel(4, 4, 9)        
        elif die_value == 4:
            display.set_pixel(0, 0, 9)
            display.set_pixel(0, 4, 9)
            display.set_pixel(4, 4, 9)        
            display.set_pixel(4, 0, 9)
        elif die_value == 5:
            display.set_pixel(0, 0, 9)
            display.set_pixel(0, 4, 9)
            display.set_pixel(2, 2, 9)
            display.set_pixel(4, 4, 9)        
            display.set_pixel(4, 0, 9)
        elif die_value == 6:
            display.set_pixel(0, 0, 9)
            display.set_pixel(0, 4, 9)
            display.set_pixel(0, 2, 9)
            display.set_pixel(4, 4, 9)        
            display.set_pixel(4, 0, 9)
            display.set_pixel(4, 2, 9)
            
   