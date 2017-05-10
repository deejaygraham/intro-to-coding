from microbit import *

small_heart = Image ("00000:05550:05650:05550:00000:")
big_heart = Image ("09090:99999:99999:09990:00900:")

heartbeat = [ small_heart, big_heart, small_heart, big_heart, small_heart, small_heart ]

display.show(heartbeat, loop=True, delay=250)    
