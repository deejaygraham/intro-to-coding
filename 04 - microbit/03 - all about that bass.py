#The bridge melody of All about that Bass by Meghan Trainor.
#Coded by Ben Mustill-Rose and Nicholas Tollervey.
from microbit import *
#As we're going to be playing music we'll need to import the music module:
import music

#All music has a tempo (how fast it is played) often given in beats per minute or BPM
#The tempo of All About That Bass is approximately 135BPM.
music.set_tempo(bpm=135)

#Parts of the chorus are repeated, so to make our program more efficient & easier to read!
#We've split the melody up into "lists" that we can use without typing all the notes out again.

#The "Yeah my momma she told me don't worry about your-" passage:
#It's also the "You know I won't be no stick-figure, silicone Barbie-" passage!
wellMyMomma=["f#4:2", "g#", "a:3", "a", "a:2", "g#:3", "g#", "g#:2",
    "f#:3", "f#", "f#:2", "e:4", "c#:2", "e"]

#The "She says: Boys, they like a little more booty to hold-" passage:
# It's also the "So, if that's what's you're into then go ahead and move-" passage!
sheSaid=["e4:2", "f#4", "g#:3", "g#", "g#:2", "f#:3", "f#", "f#:2", "e:3", "e", "e:2", "d:4"]

# "Siiiiiiize~":
size=["d4:12", "r:16"]

# "At niiiiiiight~":
atNight=["b3:2", "d4", "c#:12", "r:14"]

# "Doooolllll~":
doll=["d4:6", "c#:2", "b3:8", "r:10"]

# "Aloooooooong~":
along=["d4:2", "d4", "c#4:6", "b3:2", "a3:6"]

#Now that we've created all the lists we need for the chorus lets play some music!
#We want the chorus to play forever, we're using a "while" loop that will never exit.
while True:
  music.play(wellMyMomma) #"Yeah my momma she told me don't worry about your-"
  music.play(size) #"Size"
  music.play(sheSaid) #"She says: Boys, they like a little more booty to hold-"
  music.play(atNight) #"At night"
  music.play("e4:2") #"You-"
  music.play(wellMyMomma) #"Know I won't be no stick-figure, silicone Barbie-"
  music.play(doll) #"Doll"
  music.play(sheSaid) #"So, if that's what's you're into Then go ahead and move-"
  music.play(along) #"Along"
  music.play("r:12") #Rest for the remaining bar
    
    
#The bridge bassline of All about that Bass by Meghan Trainor.
#Coded by Ben Mustill-Rose and Nicholas Tollervey.
from microbit import *
#As we're going to be playing music we'll need to import the music module:
import music

#All music has a tempo (how fast it is played) often given in beats per minute or BPM
#The tempo of All About That Bass is approximately 135BPM.
music.set_tempo(bpm=135)

bassline = [
    'r:12',
    'a1:6', 'c2:2', 'c#', 'e:4', 'c#:2',
    'a1:4', 'r:12',
    'b1:6', 'c#2:2', 'd', 'f#:4', 'd:2',
    'b1:4', 'r:12',
    'e1:6', 'g:2', 'g#', 'b:4', 'g#:2',
    'e:4', 'r:12',
    'a1:6', 'c2:2', 'c#', 'e:4', 'c#:2',
    'a1:4'
    ] 

#We're keeping this code so simple, we're even going to skip 'while True'!
#Playing music can be looped forever by adding 'loop=True':
music.play(bassline, loop=True)

