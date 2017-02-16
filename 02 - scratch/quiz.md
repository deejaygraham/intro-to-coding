Writing a quiz

Lots of different kinds of quiz but it's good to have something with a correct answer
that we can easily tell is correct. The two kinds of quiz we could consider today are a
general knowledge quiz or a maths quiz:

We need a way to ask a question, get an answer, decide if that answer is correct
then give some feedback.

So let's get started:

Create a new project...

Simplest case possible to get us started.

New project

I'm tired of the scratch cat, so let's pick a new one from the library.
Delete the cat and select the new sprite.

Now we'll go to the sensing blocks and drag an ask block. Let's start with something simple,
a what is 2 + 2 question.

If we run this now, we can see the question is asked and a box opens up for us to type an answer.

If we want to evaluate that answer we need to use an if block from the control section.
We also need something from the operators section to check if our answer is equal to our expected value.

We can fill in the answer we want with 4 and add the answer from the sensing section.

We can then do something like, play a sound or have some kind of celebration. For ease we
can say that they are correct using the Looks section and dragging a "say"

Extensions - how do we keep score
How do we tell them they got the question wrong.
How do we extend it to more questions.
Can we make a maths challenge?

Create two new numbers, fill them in with random values.
Create an answer value which is set with n1 + n2
Hide the variables
Ask for joined text for n1 + n2
If answer = answer expected
celebrate
else
  wrong
Loop.


Now we can chain more questions together. and keep score like we did with the cat game.
