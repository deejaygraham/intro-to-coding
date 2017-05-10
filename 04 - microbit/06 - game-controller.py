from microbit import *

# accelerometer readings are +- 1000
forty_five_degrees = 500

x_tilt_limit = forty_five_degrees
y_tilt_limit = forty_five_degrees

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

def write_to_serial_port(data):
    print(data)

# display flashing middle pixel so we know 
# the device is alive
# alternate between blank display and single pixel
watch_dog_pixel = Image("00000:00000:00600:00000:00000")
watch_dog_flash = [watch_dog_pixel, Image()]

display.show(watch_dog_flash, loop=True, wait=False, delay=1000)

# Main game loop
while True:

  serial_data = ""
  serial_data += read_orientation()
  serial_data += read_buttons()

  if len(serial_data) > 0:
    write_to_serial_port(serial_data)

  sleep(100)
