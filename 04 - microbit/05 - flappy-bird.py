# Flappy Bit
# Adapted from:
# http://blog.withcode.uk/2016/05/flappy-bird-microbit-python-tutorial-for-beginners

from microbit import *
import random

# board dimensions
width, height = 5, 5

Frame_Rate_In_Milliseconds = 20
Increase_Score_After_Frames = 50
Wall_Speed = 20 # number of frames between each time a wall moves a pixel to the left
Wall_Generation_Speed = 100       # number of frames between each new wall


def display_game_over(score):
    display.show(Image.SAD)
    sleep(500)
    display.scroll("Score: " + str(score))


def bird_collides_with_wall(pipe, bird):
    if pipe.get_pixel(bird[0], bird[1]) != 0:
        return True

    return False

def hide_bird(bird): # flapping
    display.set_pixel(bird[0], bird[1], 0)

def draw_bird(bird): # flapping
    display.set_pixel(bird[0], bird[1], 9)

def display_count_down(fromValue):
    while fromValue > 0:
        display.show(fromValue)
        sleep(1000)
        fromValue -= 1
    display.clear()


display_count_down(5)

# left hand part of the screen, in the middle
# consider orientation for buttons up, down
bird = [ 1, 2 ] # x, y

draw_bird(bird)

# Global variables
y = 50
speed = 0
score = 0
frame = 0

# Make an image that represents a pipe to dodge
def make_pipe():
    # make a pipe at the far end of the screen...
    pipe = Image("00003:00003:00003:00003:00003")

    last_line_x = 4

    gap_position_y = random.randint(0, 3)               # random gap position
    pipe.set_pixel(last_line_x, gap_position_y, 0)      # make a hole in the pipe
    pipe.set_pixel(last_line_x, gap_position_y + 1, 0)  # for flappy to get through

    return pipe

# create first pipe
pipe = make_pipe()

currentFrame = 0

# Game loop
while True:

    currentFrame += 1

    # show pipe
    display.show(pipe)

    # flap if button a was pressed
    if button_a.was_pressed():
        speed = -8

    # show score if button b was pressed
    #if button_b.was_pressed():
        #display.scroll("Score:" + str(score))

    # accelerate down to terminal velocity
    speed += 1
    if speed > 2:
        speed = 2

    # move bird, but not off the edge
    y += speed
    if y > 99:
        y = 99
    if y < 0:
        y = 0

    # draw bird
    led_y = int(y / 20)
    display.set_pixel(1, led_y, 9)

    # check for collision
    if bird_collides_with_wall(pipe, bird):
        display_game_over(score)
        break

    # move wall left
    if(frame % FRAMES_PER_WALL_SHIFT == 0):
        pipe = pipe.shift_left(1)

    # create new wall
    if(frame % FRAMES_PER_NEW_WALL == 0):
        pipe = make_pipe()

    # increase score
    if (frame % Increase_Score_After_Frames) == 0:
        score += 1

    sleep(Frame_Rate_In_Milliseconds)
