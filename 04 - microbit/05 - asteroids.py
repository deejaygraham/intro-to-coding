
from microbit import *
import random

# board dimensions
pixel_width, pixel_height = 5, 5
Frame_Rate_In_Milliseconds = 500

# general game functions

def display_count_down(fromValue):
    for i in range(fromValue, 0, -1):
        display.show(str(i))
        sleep(1000)

def display_game_over(score):
    # blow up ship
    # take x of ship and blow up outwards

    display.show(Image.SAD)
    sleep(500)
    display.scroll("Score: " + str(score))

# ship functions
# bottom part of the screen, in the middle
def create_ship():
    # x, y, brightness
    return [2, 4, 9]

def hide_ship(ship):
    display.set_pixel(ship[0], ship[1], 0)

def draw_ship(ship):
    display.set_pixel(ship[0], ship[1], ship[2])

def blow_up_ship(ship):

    hide_ship(ship)

    for brightness in range(ship[2], 0, -1):
        draw_explosion(ship, brightness)
        sleep(500)

    # look at x position
def draw_explosion(centre, brightness):

    x = centre[0]
    y = centre[1]
    left_of_centre = x - 1
    right_of_centre = x + 1
    above_centre = y - 1

    if left_of_centre >= 0:
        display.set_pixel(left_of_centre, y, brightness)
        display.set_pixel(left_of_centre, above_centre, brightness)

    display.set_pixel(x, above_centre, brightness)

    if right_of_centre < pixel_width:
        display.set_pixel(right_of_centre, y, brightness)
        display.set_pixel(right_of_centre, above_centre, brightness)

# asteroid functions

def hide_asteroid(asteroid):
    display.set_pixel(asteroid[0], asteroid[1], 0)

def draw_asteroid(asteroid):
    display.set_pixel(asteroid[0], asteroid[1], asteroid[2])

def create_asteroid():
    # x, y, brightness, maybe speed.., size
    return [ random.randint(0, pixel_width), 0, random.randint(1, 8) ]

def asteroid_collides_with_ship(asteroid, ship):
    return asteroid[0] == ship[0] and asteroid[1] == ship[1]:

def move_asteroid(asteroid):
    asteroid[1] += 1
    return asteroid


score = 0

ship = create_ship()
asteroid = create_asteroid()

# gane start
display_count_down(5)
display.clear()

# Game loop
while True:

    draw_ship(ship)
    draw_asteroid(asteroid)

    sleep(Frame_Rate_In_Milliseconds)

    # check for button pushes...

    if asteroid_collides_with_ship(asteroid, ship):
        display_game_over(score)
        break

    hide_ship(ship)
    hide_asteroid(asteroid)

    if asteroid[1] == 4:
        score += 1
        asteroid = create_asteroid()

    asteroid = move_asteroid(asteroid)

    # increase speed once we are above a certain score...
