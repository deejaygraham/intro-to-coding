# Rock, Paper, Scissors
#
# Shake the microbit and it will pick 
# a shape at random.

from microbit import *

import random

def display_count_down(fromValue):
    for i in range(fromValue, 0, -1):
        display.show(str(i))
        sleep(1000)

show_pic_for = 1000
# create shapes

# rock
rock = Image("00000:"
             "09990:"
             "90009:"
             "92229:"
             "29992")
 
# paper
paper = Image("99950:"
              "90992:"
              "90092:"
              "90092:"
              "99992")

# scissors
scissors = Image("90009:"
                 "09090:"
                 "00900:"
                 "55055:"
                 "55055")



while True:
    
    # Show countdown
    #display_count_down(3)
    display.clear()

    #if accelerometer.was_gesture("shake"):
    #display.clear()
    #sleep(1000)
        
    choice = random.randrange(3)
        
    if choice == 0:
        display.show(rock)
    elif choice == 1:
        display.show(paper)
    elif choice == 2:
        display.show(scissors)
            
    sleep (show_pic_for)

