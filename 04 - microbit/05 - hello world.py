# speaker between pins 0 and 1
import speech

speech.say("Hello, World")

# timbre variables
#
# pitch - how high or low the voice sounds (0 = high, 255 = Barry White)
# speed - how quickly the device talks (0 = impossible, 255 = bedtime story)
# mouth - how tight-lipped or overtly enunciating the voice sounds (0 = ventriloquist’s dummy, 255 = Foghorn Leghorn)
# throat - how relaxed or tense is the tone of voice (0 = falling apart, 255 = totally chilled)

speech.say("I am a DALEK - EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)
