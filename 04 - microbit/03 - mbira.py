# output to speaker, wired between pins 0 and gnd

from microbit import *
import music

lownote= ["c4:4"]
highnote = ["c5:4"]

while True:
    if pin1.is_touched() and pin2.is_touched():
        tune = ["C4:4", "D4:4", "G4:8"]
        music.play(tune)
    elif pin1.is_touched():
        tune = ["C3:4", "D3:4", "G4:8"]
        music.play(tune)
    elif pin2.is_touched():
        music.play(music.BADDY)
        
    sleep(500)
    
    # adjust speed of playback
    # incorporate gestures? difficult with wiring?
    # random note if both together
    # or pre-packaged sound
    # use accelerometer to make it into a theramin.
    
