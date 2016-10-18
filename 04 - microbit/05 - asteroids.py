
from microbit import *
import random

# board dimensions
pixel_width, pixel_height = 4, 4
Frame_Rate_In_Milliseconds = 500

# general game functions

def display_count_down(fromValue):
    for i in range(fromValue, 0, -1):
        display.show(str(i))
        sleep(1000)

def display_game_over(ship, score):
    # blow up ship
    # take x of ship and blow up outwards
    blow_up_ship(ship)
    sleep(500)
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

def move_ship_left(ship):
    ship[0] = max(ship[0] - 1, 0)
    return ship

def move_ship_right(ship):
    ship[0] = min(ship[0] + 1, pixel_width)
    return ship

def blow_up_ship(ship):

    hide_ship(ship)

    draw_explosion(ship, ship[2], 1)
    sleep(200)
    display.clear()

    for brightness in range(ship[2], 0, -1):
        draw_explosion(ship, brightness, 2)
        sleep(200)
        display.clear()

    # look at x position
def draw_explosion(centre, brightness, radius):

    x = centre[0]
    y = centre[1]
    left_of_centre = x - radius
    right_of_centre = x + radius
    above_centre = y - radius

    if left_of_centre >= 0:
        display.set_pixel(left_of_centre, y, brightness)
        display.set_pixel(left_of_centre, above_centre, brightness)

    display.set_pixel(x, above_centre, brightness)

    if right_of_centre <= pixel_width:
        display.set_pixel(right_of_centre, y, brightness)
        display.set_pixel(right_of_centre, above_centre, brightness)

# asteroid functions

def hide_asteroid(asteroid):
    display.set_pixel(asteroid[0], asteroid[1], 0)

def draw_asteroid(asteroid):
    display.set_pixel(asteroid[0], asteroid[1], asteroid[2])

def create_asteroid():
    # x, y, brightness, maybe speed.., size
    minimum_brightness = 3
    maximum_brightness = 8
    return [ random.randint(0, pixel_width), 0, random.randint(minimum_brightness, maximum_brightness) ]

def asteroid_collides_with_ship(asteroid, ship):
    return (asteroid[0] == ship[0]) and (asteroid[1] == ship[1])

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

    # increase speed once we are above a certain score...
    sleep(Frame_Rate_In_Milliseconds)

    if asteroid_collides_with_ship(asteroid, ship):
        display_game_over(ship, score)
        break

    hide_ship(ship)
    hide_asteroid(asteroid)

    if asteroid[1] == pixel_height:
        score += 1
        asteroid = create_asteroid()
    else:
        # check for button pushes...
        if button_a.was_pressed():
            #display.scroll('A')
            ship = move_ship_left(ship)
            #display.scroll(str(ship[0]) + ' ' + str(ship[1]))
        elif button_b.was_pressed():
            ship = move_ship_right(ship)

        asteroid = move_asteroid(asteroid)
