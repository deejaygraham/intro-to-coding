# Scratch

1 hour

Scratch is a visual programming language that you can use to make simple programs and games. It's
aimed primarily at children but anyone can use it to get started with programming.

There are versions you can download to your machine or you can get started really quickly using the website.

Go to: [http://scratch.mit.edu](http://scratch.mit.edu)

and click on the *Create* button

![create link](scratch-create-link.png)

The left hand side is where your program will run. The middle is set of building blocks you can use to
build the program (Scripts). Right hand side is where you drag the blocks and wire them up.


Note the Start and Stop buttons at the top.

I have written the worst game in history and I am so proud, I would like to share it with you.

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

### Yes and No: Boolean Logic ???

Is it a cat or is it a sandwich. If you ask a computer, it will say yes. If you ask a person, she will say cat. computers like to think in black and white terms, yes or no, true or false. So asking if something is a cat you can get a yes or no answer, the same as if you asked a human. It begins to get more subtle when the question has more than one part. Humans are good at looking at what the question is and deciding the best way to answer it, can it be answered yes or no or is the asker looking for a different reply? Computers are lazy and like to fall back on yes and no, particularly if you are asking a yes or no-able question. If the answer could be yes or no, you will get a yes or no answer.

Breaking it down. If you ask is it a cat (yes) or a sandwich (no). Computer will look at first condition and because it is lazy will say that no matter what the second part of the question is, it can answer yes to the first bit. The or means is this thing you are asking about either one of these alternatives.

If you ask a question like is this a cat and is it tortoise shell? The and forces the computer to do a bit more work. It can look at the thing and see if it is a cat. If it's not, it can answer no straightaway because there is no way it needs to work out the next bit, a simple no is all it requires. If it is a cat, it then it has to look at the cat's colour and work out if there is a match. Asking AND means does this thing have all the qualities I am asking about.

We aren't restricted to asking questions about a single object at a time. We can ask is that a cat and is that other thing a bus? Is that a cat and is the sky blue?
The same process goes on whatever the conditions. We can even build up more elaborate conditions if we want to.


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

### What did we learning

Decomposing a game into smaller parts.
Putting things in the right order - sequence
selection - is it on an edge?
Repetition - keep going
Variables - score, location, speed, colour
Events - program start, end, mouse click, mouse move.

### Resources

Raspberry Pi website has lots of good scratch material that is not RP specific.

https://www.raspberrypi.org/learning/getting-started-with-scratch/
