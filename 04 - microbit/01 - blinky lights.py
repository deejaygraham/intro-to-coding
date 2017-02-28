from microbit import *

lights_on = Image(
            "90000:"
            "09000:"
            "00900:"
            "00090:"
            "00009")

while True:
    display.show(lights_on)
    sleep(500)
    display.clear()
    sleep(500)
