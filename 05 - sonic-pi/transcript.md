# Sonic Pi

Sonic Pi developed Sam Aaron, developed to make music programming accessible and give fast feedback to young people experimenting with computers. His experience has been that even the most disengaged students can find something that captures their imagination in the music environment.

Simplest programming language, using sound and music for instant feedback without all the
clutter of more grown up languages. Easy first step into "real" programming. Real programming you are usually writing text in some kind of editor (think writing document like using Word but instead of sending it to printer or to human via email) and then asking the computer to do what it does.


Download it from:

[http://sonic-pi.net](http://sonic-pi.net)

Comes with lots of great help, example code you can cut and paste and run. If you get stuck, look at the help and see if there's code you can steal and adapt to what you want.

Notice code area, buttons along the top and execution area at the side.


## First Program

~~~

play 60

~~~

Press the Run button when you are done typing.

Our first program, plays a note and then stops. Not very exciting but we have written some text, had the computer read it, understand it and decide what to do with it. **Play** is an instruction and **60** is data. We can use the same instruction and give it different data for a different outcome.

We can change the value 0 - 255 and see what changes about the sound we hear. So we can see that the number represents a pitch or a musical note.

What happens is we deliberately spell play wrong? What happens when we fix it?


## Second Program

Another way to represent pitches, in a more intuitive way, is using names of notes. There's a special notation for this. 48 maps to the note C and it's in the third octave, so we say it's C3. Like this:

~~~

play :C4

~~~

Make sure you have a colon in there as well. That's just to tell the computer that the next thing is something it should recognize as a special thing.

### incidentals

Note that incidentals are available, sharps use an ‘s’ in between the note name and the octave, flats use a ‘b’.

~~~

play :Cs5
sleep 0.5
play :Eb5
sleep 0.5

~~~

Finally, especially if you are delving into algorithmic composition, you can play with a note value defined in a variable:

~~~

middle_c = 60

play middle_c
sleep 0.5

~~~


![map](midi-mapping.jpg)


### Rests

Music is about more than notes, it's also about the gaps between notes. Type this

~~~

play :C4
sleep 1
play :C4
sleep 1

~~~

What does the 1 represent. It's not a note value now, we are using a number to represent a time interval.
In same way we changed the note value, we can change the sleep value.

What happens when you increase or decrease the time? Use 10 or try 0.25

Smaller values give shorter wait times. We are using the same numbers in different ways - different abstractions.

Playing notes one after another gives us a tune.


## Simple Tunes

Not very exciting is it? How about if we add some more notes?

~~~

play :C4
sleep 1
play :C4
sleep 1
play :G4
sleep 1
play :G4
sleep 1
play :A4
sleep 1
play :A4
sleep 1
play :G4
sleep 2

~~~

Notice the last note is longer than the others because we have given the note twice the length of the others.

Anybody guess what the tune is?


### And Complete It

![twinkle](twinkle-twinkle-little-star.png)

Can you complete the tune? Or add more to it? Maybe work in pairs.


### Tidying up

This code is starting to get a bit unwieldy, it could do with some tidying up. How about we change twinkle twinkle to make it a bit nicer.

We can set up our timing so that we only need to change the time values in one place.

~~~

root = 60
quarter_note = 1
half_note = quarter_note * 2

~~~

We can also notice that we are repeating notes so we can do something like:

~~~

2.times do
  play root
  sleep quarter_note
end

2.times do
  play root + 7
  sleep quarter_note
end

2.times do
  play root + 9
  sleep quarter_note
end

play root + 7
sleep half_note

~~~

We have cut down the notes almost in half. If we need to change something, we have chunks that are easier to reason about.

or we could use:

~~~

play_pattern_timed [ :C4, :C4, :G4, :G4, :A4, :A4, :G4 ], [ 1, 1, 1, 1, 1, 1, 2 ]

~~~

If the delay between notes is the same we can shorten it to:

~~~~

play_pattern_timed [ :C4, :G4 ], 0.5

~~~~

## Play a Scale

We can play a chromatic (every note) scale like running all the way up a piano keyboard like this:

~~~

root = 36
note = root

12.times do
  play note
  sleep 0.5
  note += 1
end

~~~

Of course, sonic pi also has a scale function built in, to save you from the maths:

~~~

play scale(:c3, :major)

~~~


## Halloween Challenge

Sonic Pi really is a music programming languagae and let's you make all sorts of music.

In honour of halloween, here's a quick version of the "villain" trope from the silent movies but you might also recognize from cartoons.

![villain](mysterioso-pizzicato.png)

~~~

use_synth :piano

speed = 0.65  #set overall speed


minim = 2 * speed
crotchet = 1 * speed
quaver = 0.5 * speed

2.times do
  play_pattern_timed [:A3, :C4, :E4, :A4], crotchet
  play :F4
  sleep minim
  play_pattern_timed [:E4, :D4, :C4, :B3 ], quaver
end

play :A3
sleep crotchet

~~~

### Chords

A chord is a collection of notes played at the same time. Because it is a collection, sonic pi uses the same list notation that the play_pattern function used:

~~~

play_chord [ :C3, G3, :C4 ] # power chords !!!

~~~

You can also use chords explicitly, let's play the notes in a chord...

~~~

chord(:e3, :major7).each do |n|
  play n
  sleep 0.5
end

play chord(:e3, :major7)
sleep 2

~~~


## Random

We can talk about randomizing notes by using the **rrand_i** function. This is a built in function that will give us back a random value between 50 and 95 every time we ask for it.

~~~

8.times do
  play rrand_i(50, 95)
  sleep 0.125
end

~~~

We can make things sound a little bit more musical by only picking notes that belong to a chord:

~~~

loop do
  play chord(:a3, :minor).choose,
  sleep 0.2
end

~~~

## Live Loops

We can use samples, different synthesizers etc. to make more interesting sounds and use
algorithms to vary the music.

~~~

use_bpm 52
use_synth :piano

live_loop :bass do
  [:d2, :a2, :b2, :g2].each do |note|
    8.times do
      play note, release: 0.2
      sleep 0.25
    end
  end
end

~~~

We can put that together with another loop to give us a drum and base theme

### Samples

~~~

live_loop :kick do
  sample :drum_bass_hard
  with_fx :slicer do
    sample :drum_bass_hard
  end
  sleep 0.5
end

~~~


## Synths

All of the sounds so far have been using the default sound from a synthesizer called beep. We can use any kind of synthesizer we want using

~~~

use_synth :piano

~~~

There's much more to be explored here but I hope that has given you some ideas for what can be done.


## Frozen

If you really get into composition this way, there's lots you can do. Here's a version of the Disney song "Let it Go" from the film "Frozen"


### What Have We Learned?

* Predicting Behaviour
* Putting things in the right order - sequence
* Selection - is it on an edge, is the game over?
* Repetition - iteration blocks, loops
* Variables - notes, rests
* Abstraction - is it a note, is it a time value. We are using a number to represent a musical note's value. This is what we mean by abstraction. We are using a number in place of a concept in the real world.

### Resources

[http://sonic-pi.net](http://sonic-pi.net)
