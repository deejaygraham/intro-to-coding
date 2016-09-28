from microbit import *

table_edge = 4
table_centre = 2

def keep_ball_on_table(ball):
    # bounds of led grid
    ball[0] = min(ball[0], table_edge)
    ball[0] = max(ball[0], 0)
    ball[1] = min(ball[1], table_edge)
    ball[1] = max(ball[1], 0)

    return ball

# Accelerometer
def tilt_is_slight(tilt):
    return abs(tilt) < 50

def tilt_is_left(tilt):
    return tilt < 0

def tilt_is_right(tilt):
    return tilt > 0

def tilt_is_up(tilt):
    return tilt > 0

def tilt_is_down(tilt):
    return tilt < 0

# drawing
refresh_in_milliseconds = 50

PIXEL_ON = 9
PIXEL_OFF = 0

def hide_ball_at(point):
    display.set_pixel(point[0], point[1], PIXEL_OFF)

def show_ball_at(point):
    display.set_pixel(point[0], point[1], PIXEL_ON)

display.clear()

# start in centre
ball = [ table_centre, table_centre ]

#light up the centre dot...
show_ball_at(ball)

while True:

    sleep(refresh_in_milliseconds)

    hide_ball_at(ball)

    x_tilt = accelerometer.get_x()
    y_tilt = accelerometer.get_y()

    if tilt_is_slight(x_tilt):
        ball[0] = ball[0] # nothing
    elif tilt_is_left(x_tilt):
        ball[0] -=
    elif tilt_is_right(x_tilt):
        ball[0] += 1

    if tilt_is_slight(y_tilt):
        ball[1] = ball[1] # nothing
    elif tilt_is_left(y_tilt):
        ball[1] -= 1
    elif tilt_is_right(y_tilt):
        ball[1] += 1

    ball = keep_ball_on_table(ball)

    # calibraton
    #display.scroll(str(x_tilt) + " " + str(y_tilt))
    show_ball_at(ball)

    if ball[0] == table_centre and ball[1] == table_centre:
        sleep(1000)
        display.show(Image.HAPPY)
        sleep(2000)
        display.clear()
