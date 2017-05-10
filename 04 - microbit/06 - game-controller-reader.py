# game controller reader, reading from usb-attached microbit

# Run dmesg from console
# Plug in microbit to usb port

# look for tty entry e.g. ttyACM0 is /dev/ttyACM0
# ls /dev/ttyA*

# install pyserial
# sudo apt-get install python-pyserial

import serial

# change this! !!
device = '/dev/ttyACM0'
baud_rate = 115200

serial_port = serial.Serial(device, baud_rate, timeout = 1)

def read_serial_port():

    encoded_command = ""

    received = serial_port.readline()

    if received:
        encoded_command = received.decode('utf-8').rstrip()

    return encoded_command


#while True:
#    received = serial_port.readline()

#    if received:
#        encoded_command = received.decode('utf-8').rstrip()
        # do something with it


#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__":

    while True:
        coded_bits = read_serial_port()
        if coded_bits:
            if 'U' in coded_bits: print("up")
            if 'D' in coded_bits: print("down")
            if 'L' in coded_bits: print("left")
            if 'R' in coded_bits: print("right")
            if 'A' in coded_bits: print("fire")
            if 'B' in coded_bits: print("eject")
