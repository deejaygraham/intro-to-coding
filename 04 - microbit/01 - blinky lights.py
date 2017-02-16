from microbit import *

lights_on = Image(
            "99999:"
            "99999:"
            "99999:"
            "99999:"
            "99999")

while True:
    display.show(lights_on)
    sleep(500)
    display.clear()
    sleep(500)
