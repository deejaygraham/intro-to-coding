from microbit import *

x_tilt_limit = 500
y_tilt_limit = 500

def read_orientation():

  orientation = ""

  x = accelerometer.get_x()

  if x < -x_tilt_limit:
    orientation += 'L'
  elif x > x_tilt_limit:
    orientation += 'R'

  y = accelerometer.get_y()

  if y < -y_tilt_limit:
    orientation += 'D'
  elif y > y_tilt_limit:
      orientation += 'U'

  return orientation

def read_buttons():

    buttons = ""

    if button_a.is_pressed():
      buttons += 'A'

    if button_b.is_pressed():
      buttons += 'B'

    return buttons

# blink one pixel to show the controller is alive
def watch_dog():

    centre_pixel = [2, 2]
    brightness = display.get_pixel(centre_pixel[0], centre_pixel[0])

    if brightness == 0:
        brightness = 9
    else:
        brightness = 0

    display.set_pixel(centre_pixel[0], centre_pixel[0], brightness)

def write_to_serial_port(data):
    print(data)

# Main game loop
while True:

  serial_data = ""
  serial_data += read_orientation()
  serial_data += read_buttons()

  if len(serial_data) > 0:
    write_to_serial_port(serial_data)

  watch_dog()
  sleep(100)
