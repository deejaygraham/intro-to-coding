# piezo speaker between pin 0 and ground
# button a to speed up button b to slow down

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(20)
    pin0.write_digital(0)
    sleep(480)
    
