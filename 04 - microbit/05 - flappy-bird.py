# Flappy Bit
# Adapted from:
# http://blog.withcode.uk/2016/05/flappy-bird-microbit-python-tutorial-for-beginners

from microbit import *
import random

# board dimensions
pixel_width, pixel_height = 5, 5
Frame_Rate_In_Milliseconds = 20

# general game functions

def increase_score_if_required(frame, score):
    Increase_Score_After_Frames = 50
    
    if (frame % Increase_Score_After_Frames) == 0:
        return score + 1
        
    return score
    
def display_count_down(fromValue):
    while fromValue > 0:
        display.show(fromValue)
        sleep(1000)
        fromValue -= 1
    display.clear()

def display_game_over(score):
    display.show(Image.SAD)
    sleep(500)
    display.scroll("Score: " + str(score))# wall functions

# bird functions

def hide_bird(bird): # flapping
    display.set_pixel(bird[0], bird[1], 0)

def draw_bird(bird): # flapping
    display.set_pixel(bird[0], bird[1], 9)

# wall functions

def draw_wall(wall):
    display.show(wall)
    
def should_create_wall(frame):
    Wall_Created_After_Every = 100 
    return (frame % Wall_Created_After_Every) == 0    

def create_wall():
    # create an image of a wall at the far end of the screen...
    wall = Image("00003:00003:00003:00003:00003")
    
    # make a hole in the wall
    # for flappy to get through
    hole_in_the_wall_y = random.randint(0, pixel_height - 2) 
    wall.set_pixel(pixel_width - 1, hole_in_the_wall_y, 0)      
    wall.set_pixel(pixel_width - 1, hole_in_the_wall_y + 1, 0)  

    return wall

def bird_collides_with_wall(bird, wall):
    if wall.get_pixel(bird[0], bird[1]) != 0:
        return True

    return False

def should_wall_move(frame):
    Wall_Moves_After_Every = 20 # number of frames between each time a wall moves a pixel to the left
    return (frame % Wall_Moves_After_Every) == 0

def move_wall(wall):
    return wall.shift_left(1)    

def calculate_gravity(gravity):

    if button_a.was_pressed():
        Flapping_Value = 8
        gravity -= Flapping_Value
        
    gravity += 1
    
    Max_Gravity = 2
    
    if gravity > Max_Gravity:
        gravity = Max_Gravity
    
    return gravity

def calculate_new_displacement(displacement, gravity):

    displacement += gravity

    Max_Displacement = 99
    Min_Displacement = 0
    
    if displacement > Max_Displacement:
        y = Max_Displacement
        
    if displacement < Min_Displacement:
        displacement = Min_Displacement
        
    return displacement

    
# left hand part of the screen, in the middle
# consider orientation for buttons up, down
bird = [ 1, 2 ] # x, y
wall = create_wall()

gravity = 0
displacement = 50

score = 0
frameCounter = 0

# gane start
display_count_down(5)
draw_bird(bird)

# Game loop
while True:

    hide_bird(bird)
    
    frameCounter += 1

    draw_wall(wall)

    gravity = calculate_gravity(gravity)
    displacement = calculate_new_displacement(displacement, gravity)
    bird[1] = int(displacement / 20)

    draw_bird(bird)

    # check for collision
    if bird_collides_with_wall(bird, wall):
        display_game_over(score)
        break

    if should_wall_move(frameCounter):
        wall = move_wall(wall)

    if should_create_wall(frameCounter):
        wall = create_wall()
        
    score = increase_score_if_required(frameCounter, score)

    sleep(Frame_Rate_In_Milliseconds)
