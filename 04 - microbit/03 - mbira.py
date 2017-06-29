# output to speaker, wired between pins 0 and gnd

from microbit import *
import music

# twinkle twinkle 
while True:
    if pin1.is_touched() and pin2.is_touched():
        tune = ["C4:4"]
        music.play(tune)
    elif pin1.is_touched():
        tune = ["G4:4"]
        music.play(tune)
    elif pin2.is_touched():
        tune = ["A4:4"]
        music.play(tune)
    elif button_a.was_pressed():
        tune = ["F4:4"]
        music.play(tune)
    elif button_b.was_pressed():
        tune = ["E4:4"]
        music.play(tune)
        
    sleep(100)
    
    # adjust speed of playback
    # incorporate gestures? difficult with wiring?
    # random note if both together
    # or pre-packaged sound
    # use accelerometer to make it into a theramin.
    
