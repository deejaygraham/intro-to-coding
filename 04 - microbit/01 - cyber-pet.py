from microbit import *

# Shake to wake your pet up
while True:

    if accelerometer.was_gesture("shake"):
        display.show(Image.HAPPY)
        sleep(1000)
    else:
        display.show(Image.ASLEEP)
