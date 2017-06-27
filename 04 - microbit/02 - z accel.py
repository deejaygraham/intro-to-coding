from microbit import *

#sea_level = 0
#top = 0

#display.scroll('press a at sea level')
# sea_level may be bigger than top???


while True:
    
    if button_a.was_pressed() or button_b.was_pressed():
        z = accelerometer.get_z()
        display.scroll(str(z))
