import time
import grovepi
from grove_rgb_lcd import *
from Hologram.HologramCloud import HologramCloud

# Establish a cellular connection
credentials = {'devicekey': 'xxxx'}
hologram = HologramCloud(credentials, network='cellular')

# Connect to port D3, which as digital pins 1 and 2

setRGB(0, 255, 0)
pir_sensor = 3
motion = 0
grovepi.pinMode(pir_sensor, "INPUT")

while True:
    try:
        # Sense motion, usually human, within the target range
        motion = grovepi.digitalRead(pir_sensor)
        if motion == 0 or motion == 1:  # check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
            if motion == 1:
                response_code = hologram.sendMessage("Motion Detected")
                setText_norefresh("Motion Detected")
            else:
                setText_norefresh("")

        time.sleep(10)

    except IOError:
        print("Error")