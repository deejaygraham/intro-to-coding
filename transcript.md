# Intro to Coding

## Welcome

Hi, welcome to this introductory session on coding.

### Me

My name is Derek Graham and I am a principal developer at Sage. I've spent the last 25 years developing software for lots of different industries, products and worked in lots of different areas - consulting, managing teams and software departments, and sometimes writing code. I have a BSc. in Electronics and Physics and an MSc. in Computer Science.

### Introductions

I know for this session you all know each other, but to get a sense of everyone else's current experience and expectations, can we go around the room and just say who you are, what your experience is (if any) and what you hope to get out of this afternoon?

### My Vision

My vision for this afternoon is to bring you up to date on the last 200 years of computing history and why we are where we are today. To talk about making first steps into learning about computer science, we'll take a look at some of the best languages for new learners available at the moment and I hope to give you lots of ideas for how to teach this subject when you get back to school.

I don't want to spend any longer than necessary talking today, what I would like is to explain some things, then have you tinker and explore enough to feel comfortable that you aren't just following a list of instructions but beginning to understand what it's all about.

We're going to play with some code, make some things, break some things (maybe on purpose and definitely by accident) and put then them back together. We'll make lots of mistakes, go down blind alleys and hopefully discover some stuff. I want you to be fiddling with code, taking it apart to see how it works. You can't break anything and the worst thing that can happen is that we have to scrap your program and type it in again. No one will shout at you for getting something wrong. By making those mistakes you will get a better understanding of what is going on inside the mind of the computer and if something goes wrong it's not the end of the world, no one will die and no one will be eaten. It is normal for some of this to hurt your head to begin with but struggling with some of these concepts isn't anything to be frightened of but rather embraced. Programming (and understanding what is going on inside a computer) is a skill like any other. You don't have to be special to learn how to do it but it does take a little bit of time and effort to get used to applying that skill. Most of the work is going to be inside your head, not typing keys on the keyboard.

### Computers in Society

Most people's ideas about computers come either from the movies (hackers) or from being made to use awful software in their own work, frequently badly designed software that makes them feel stupid for not knowing how to use it correctly.

Otherwise in popular culture and in the news, it's about building mobile apps or websites or where the latest security leak has happened. For me it's a hugely social and creative outlet and very much about self-expression.

One example of the extreme creative side of coding is Sam Aaron, inventor of sonic pi (later), who writes code in nightclubs all over the world. His code creates music which he performs live in front
club goers who usually can't tell it from a conventional dj.




The more approachable we feel technology is, the more we play with it, take them apart, tinker with them, the better we a sense of what's possible we have.

### Code, Code Everywhere

Technology affects everything, AI in amazon recommendations, credit card fraud, making movies, medical research (data collection, analysis), medical devices (hearing aids), space exploration, home (Nest, Wifi, DVR), Cars (brakes, steering, engine control), iPods and mobiles

### Skills

Social skills, like making a movie - lots of specialised skills coming together with a common objective and working together and communicating. Not about working in your bedroom any more (if it ever was).

Debugging good to confirm you version of reality. Often we think we have said one thing, the other person has understood something totally different

## History

30 minutes

Mozart the dead composer wrote his programs in standard music notation. Thats really what music is,
a written set of instructions for a human and a machine to carry out together. Human plays violin, piano etc. and even though Mozart is now dead, we can
still enjoy his music provided the musicians are able to carry out his instructions to the letter (with some interpretation). No one needs the ghost of the composer to be present to make sure that the "code"
runs.

The history of computers has been the history of humans telling machines what to do. In taking you through an extremely short history, I'd like to call out the contribution of women in this field because it isn't as well represented or understood as it should be.

### Witchcraft

Super-Computer inventor Danny Hillis described what computer programmers do as being akin to witchcraft. We carve special markings onto rocks (silicon chips), speak a special arcane language them (code) and they do what we tell them out in the world (programs). If that's not witchcraft, what is? To be a computer programmer in the 16th century would have seen you burnt at the stake.

### Looms

In the 1800s the Jacquard Loom was one of the first machines that didn't need a human operator, the pattern on the carpet or rug was defined, line by line by a series of cards with holds punched in them to indicate what the design should be. The machine started at the beginning of the stack and worked it's way through each one, line by line until it reached the end and the carpet was complete.

Before this time, machines were really meant as extensions of a person's capability and required their skill to use them. Lots of machines were made after the jacquard loom, still as single purpose devices but with some kind of configuration built into them. But you could not take a windmill and make it into a bakery.

### Babbage

In the 1830s, Charles Babbage had an idea for a more general purpose maths calculation machine. He got cash from parliament to build the machine (millions of pounds) but got bored with it half way through and started another project. It was never fully built and tested until fairly recently.

Despite not having a working machine, Ada Lovelace became the first programmer to write code for a "computer" in the 1840s and the machine didn't even exist!

### War

Lots of history goes by with machines becoming more complex and having more variability and control but they tended to stay in their little silos until WWII

WW II - As the Nazi's had come up with a fiendish plot to encrypt all their data, the good folk of Bletchley Park came together to try and solve the problem using Maths. Very interesting history and not revealed until the 1980s when it came into the daylight from the cover of the official secrets act.

### Turing's Universal Machine
Alan Turing had some thoughts about general purpose computing and posed the idea that you could build a machine that would know how to carry out a very small set of instructions but that the instructions would be structured in a way that they could be combined in lots of ways so that *any* problem could be solved by it if you could work out what the list of instructions should be. Like Babbage, Turing didn't build the computer, that was a team from the Post Office headed by an electrical engineer named Tommy Flowers. They built "Collosus" which was the first proper digital computer and helped with the war.

Lots of other efforts were going on in the US and around the world to solve the same problem so history can be quite hard fought for who has the honour of first "what".

Notable in these is Jean Bartik and the (all female) crew of the ENIAC which was a digital computer used to simulate bullet trajectories for wartime. Prior to this a computer was a person with a calculator using log table to work out trajectories in about a week. The ENIAC could do it before the shell landed.

### Bugs

Things that go wrong with code where we there is an outcome that we don't intend are called bugs. This comes from a time when computers were mostly electrical and electronics writ large, lots of wires,
switches, relays and valves. The first bug was literally an insect that got caught inside the workings
of an early machine and stopped it behaving as the programmers had intended. There is never any relation to rabbits.

### To the Moon and back

One part of JFK's mission to land a man on the moon that often isn't given enough credit is the guidance system that did all the calculations in real time to plot the path from the earth to the moon as both of them were speeding through space, turing around each other and around the sun. The computer that did that had less than 1 millionth the power of your mobile phone and nowhere near as much memory. The team lead on that project was a woman called Margaret Hamilton and the team had huge number of physical challenges that modern programmers just dont face today. One was the need to store the programs and data needed on the flight in memory. The only way to store that much memory at the time was in knitted memory, iron cores were magnetized and slotted into a woven matrix to create a binary image of the program.

### Modern Space !

Space exploration without humans and Mars in particular continues to be an area where software is crucial.  The Mars rover robots are all software controlled and mostly autonomous. Calculations of trajectories earth -> mars are all software (very complicated maths).

and another woman is notable for writing the parachute guidance systems in the recent mars mission where rovers were dropped from parachutes onto surface.

### Now

All this time, the processing of machines has got faster and faster as electronics have improved, got smaller, lighter, more reliable. We've gone from hard wired - physical wiring to switches, punched cards, paper tapes etc. so getting information into the machine and getting results back out has always been a challenge. Graphs drawn, lights, beeps and boops.

Often now the same computer in your DVR or x-box is the same as in your laptop but with different input controls and outputs and different software.

Errors

Also because of turings idea of the general purpose computer being able to work on any problem, there are usually many more ways to write a program. Some will run faster than others, some will use more resources and some bad ones will do both.

Programming languages are the struggle we humans have to tell computers how to work and still be able to reason about what we have written and allow others to understand what we have done and build upon it. Communication with other humans is at least as important.

Time Flies like an arrow
Fruit Flies like a banana

How do we interpret that?


Clear, careful thinking.

How do we represent data. What should the logic be. What should be the flow, what needs to happen first, what should come later?

## Unplugged

1 hour

We don't need a computer or any electronics

Important skills for critical thinking, logic and visualization and imagination

Pencil and paper debugging
Rubber Ducking - explaining the problem and what might be the cause of it.

Using the scientific method
Hypothesis.If that'strue what would we expect - look for ways your theory confirms what you see. Look for ways it contradicts what you see.


Algoritjms

Put things in the gith ordder


Have a bath
Bathing
Turn bath water on
Get into Bath
Wash
Get out of the Bath

Have a birthday party
Set plates
Set knives and forks
bring out the food
spread the table cloth

Eat at restaurant

Eat food
Full?
No
Yes
Pay bill
Leave

Make a sandwich



Role play
Boolean logic

Different robots understand different instructions. Some are mathematical, some are more general,
some know about tea and milk, others can do the same job but need to be told exactly wehre to go
exact positions, exact commands. High level vs low level languages.


## Scratch

1 hour

Scratch is a visual programming language that you can use to make simple programs and games. It is
aimed primarily at children but anyone is able to participate and use it.

There are versions you can download to your machine or you can get started really quickly using the website.

Go to:

http://scratch.mit.edu

and click on the *Create* button

Left hand side is where your program will run. Middle is set of building blocks you can use to
build the program (Scripts). Right hand side is where you drag the blocks and wire them up.

Start and Stop buttons at the top.

### Make the cat walk

Drag move step across to right hand side and click on it with mouse. You should see the cat move a little bit.
Play with changing the value in the box. What happens? What about a negative value?

What do you think will happen?

*Variable*

### Really make it walk

Switch to the control section and drag a repeat block. Slide move into repeat block.
Click on assembled blocks. What happens? Change the repeat value.

Let's make it walk all the way across the screen. Change repeat to a forever loop.
Pull movement block out and drag repeat block out. Drag on the forever loop.

Click on block - will go off screen and you can drag it back on but it will keep trying
to escape!!!

Lets try to correct that. Go to motion blocks and use if on edge, bounce.
Now it's upside down!

Go to info on sprite and change rotation symbol to left right.


*Repetition*
*Predicting Behaviour*

### Bit Rubbish

Now that it's behaving like we want let's try and make it more realistic. For a
cartoon cat.

Costume 1
move 10
Wait 0.25
switch costume 2
move 10
wait 0.25

*Repetition*

Is there a better way - algorithm works but is a better way?  Next Costume. and remove other blocks

Notice when you have a block of blocks, you have to disassemble them from the bottom
can't get rid of the top block on it's own!

Looks better? What about the wait, we can make that zero?

### Events

Let's make it start when we start the game, rather than when we click on it.
What about if we clicked on cat?

### Game

Let's try keeping the mouse moving and if the cat catches up with you, it scores a point!

Add *point towards mouse pointer* at end of blocks.

Follows you around the screen.

How does it catch you?

Test where mouse pointer and cat are.

In sensing, there is a *touching* block. Add If block (from control) and slot in the
touching. See that it will do something inside it when the touching is true?

### Keeping Score

Make Variable from data. Score for this sprite only. Initialise at beginning.
If touching, change score by 1.

### Boolean Logic ???


### Let's end this:

Bit too easy for cat, when score increases, move cat away again. Go to random position.

Now, what about if we get to a big value?

Let's put in a check to say we will end the game when we get to 50? If operators
comparison. Add MaxScore variable. Set it to 50 at start. If Score > MaxScore then end.
Stop this script.

How could we make the game ending better? You win?


### Turtles

Use *Pens* to draw pretty pictures

Maths figures, moving around in relative space. Using angles and distances. Draw a square. Draw a triangle, draw more shapes.

Turn n degrees, move forward, turn n degrees



### Resources

Raspberry Pi website has lots of good scratch material that is not RP specific.

https://www.raspberrypi.org/learning/getting-started-with-scratch/


## Kodu

10 minutes

MS advanced game platform. Targeted at older children but still drag, drop visual
coding. Only seems to be windows specific and x-box in the US only. No website version available. Similar to
Scratch is approach - blocks drag and drop and connected together but can be used with 3-d graphics for games.

Suited to older children but not that impressive.


## Micro:bit

1 hour

This is a relatively new hardware platform - a tiny board (a bit like the raspberry pi) but
with bluetooth, compass, tiny display, accelerometer.

Unlike Scratch, which is almost entirely visual, programming the microbit is edging closer to
"real" programming using a text-based language called Micro Python.

We will try running some simple programs and a few games and look at how this text based language is different from the visual ones we've been looking at up to now.

Where Scratch scratch hid a lot of complexity behind snap together lego pieces, we
are going to be writing closer to actual instructions. Where Scratch was interpreting our commands
"live" and we could make changes that were instantly reflected in the behaviour of the program,
Micro Python is a compiled language and follows a different lifecycle. We write code in text,
we send the code down to the device where it is compiled into it's own internal representation,
then the program executes. This is faster to run and only needs to be downloaded once for each
version, but it's not as reactive and live as Scratch.

Download from http://codewith.me. connect to pc with usb cable.

Type code into window and press flash to download.

Errors are shown scrolling across the screen on the device.

Show a picture

Show a picture
delay
Show a different picture

Run forever with while true

Run until button pushed

Play with it

Change the picture on an event

Can we clean it up.

Example games:

Displaying letter
Display scrolling text
Sleep
Reacting to events

Simple Tamagotchi

Magic 8 ball

balancing ball - play and adapt it. Make it more responsive, less responsive.

flappy bird


## Sonic Pi

1 hour - Only if we have enough time.

Simplest programming language, using sound and music for instant feedback without all the
clutter of more grown up languages.

### First Program

~~~

play 55

~~~

Done. Boom!

Play is a built-in function that can run anytime we want. Here the value 55 represents a pitch or note.
Pitches can be high or low, so if we lower the value do we get a lower note?

~~~

play 40

~~~

Yes! similarly if we raise the value, does the note get higher?


~~~

play 70

~~~

Yes!

Ok, so we are using a number to represent a musical note's value. This is what we mean by
abstraction. We are using a number in place of a concept in the real world.

### Second Program

~~~

play 55
sleep 1
play 60

~~~

Delay between notes. Here the value represents an amount of time (1 second). In same
way we changed the note value, we can change the sleep value. Smaller values give shorter wait
times. We are using the same numbers in different ways - different abstractions.

Playing notes one after another gives us a tune.

We can also use colon and a letter and number combination to represent a note in a more
intuitive way:

~~~

play :C5
sleep 0.5

~~~

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

### Sequences

Sequences of single notes are played using play_pattern or play_pattern_timed. If you are using a specific tempo, you can use play_timed to play a sequence of notes using the current tempo. The notes are written as a comma delimited list:

~~~

play_pattern [40, 45, 44, 43]

~~~

If you prefer to explicitly specify timing, you can use play_pattern_timed and give individual delays between each pair of notes. Playing these two notes one after another:


~~~

play 60
sleep 0.5
play 65
sleep 0.75

~~~

is the same as this:

~~~

play_pattern_timed [60, 65], [0.5, 0.75]

~~~

If the delay between notes is the same we can shorten it to:

~~~~

play_pattern_timed [60, 65], 0.5

~~~~

We can also cycle the timing between values in the timing list by providing fewer timing values than note values.

~~~

play_pattern_timed [60, 65, 60, 62], [0.5, 0.2]

~~~

will alternate between delays of 0.5 and 0.2 seconds for each pair of notes. Using play_pattern makes the code more readable, you can keep related groups of notes together rather than long passages of single play/sleep pairs.

### Scales

~~~

root = 36
note = root

12.times do
  play note
  sleep 0.5
  note += 1
end

~~~

### Chords

A chord is a collection of notes played at the same time. Because it is a collection, sonic pi uses the same list notation that the play_pattern function used:

~~~

play_chord [ :C3, G3, :C4 ] # power chords !!!

~~~


### Elaboration

Spooky directly from sheet music

~~~
use_synth :piano

speed = 0.65  # set overall speed

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

### Further

We can use samples, different synthesizers etc. to make more interesting sounds and use
algorithms to vary the music.


## What we did

predicting behaviour
Learned about Sequencing
Looping
abstractions and models of the world
algorithms


## Review

10 minutes

What have we done today?

history

Running unplugged sessions

Sequencing
algorithms
Selection
Iteration
Variables

How to incorporate some o these things into your lesson plans and have a
appreciation for what it takes to understand what is going on inside the computer.



## Outro

10 minutes

### Things wot we have learned

algorithms
precise and unambiguous language
logic

decompose a problem into smaller steps

create simple programs
use logical reasoning to predict behaviour of a program

sequence
Selection
repetition
Variables

using abstraction to model the world to solve a problem

Different kinds of programming languages
  Interpreted
  Compiled

Inputs
outputs

debug simple programs


## Resources

### Books

The Pattern on the Stone, W. Daniel Hillis

A Mind of It's Own - Cordelia Fine

Brain Rules - John Medina

Agile thinking and learning, Andy Hunt, Pragmatic programmers

### Videos

Background

Jean Bartik and the ENIAC women
https://www.youtube.com/watch?v=aPweFhhXFvY

Longer interview with Jean Bartik
https://www.youtube.com/watch?v=buAYHonF968


### Websites

Scratch
http://scratch.mit.edu

Kodu
http://www.kodugamelab.com/

Micro:bit
http://codewith.mu/


Micro:bit and MicroPython Help
http://microbit-micropython.readthedocs.io/en/latest/index.html

Microbit for Primary Schools: http://mb4ps.co.uk/

Multi Wing Span - Microbit examples, games
http://www.multiwingspan.co.uk/micro.php

Sonic Pi
http://sonic-pi.net/

HTML
Sarah Frisk comic about coding web pages:
http://monstermarkupmanual.com/

Hour of Code
Lesson plans, advice on organizing one-off events
https://code.org/

Code Club
https://www.codeclub.org.uk/

Twinery - create interactive games or short stories using javascript and html.
https://twinery.org/

Project Spark
http://welcome.projectspark.com/

## Resources

Notes on "How to Train your Robot"
http://drtechniko.com/2012/04/09/how-to-train-your-robot/
