from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
from Hologram.HologramCloud import HologramCloud

# Provide Hologram device key
credentials = {'devicekey': 'xxxxxxxx'}
hologram = HologramCloud(credentials, network='cellular')

dht_sensor_port = 3  # connect the DHt sensor to port 3
dht_sensor_type = 0  # use 0 for the blue-colored sensor

# set green as backlight color
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(0, 255, 0)

while True:
    try:
        # get the temperature and Humidity from the DHT sensor
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)

        # display temperature and humidity values on LCD

        if temp > 0.0:
            setText_norefresh("Temp:" + str(temp) + "C      " + "Humidity :" + str(hum) + "%")

        if temp > 45:
            response_code = hologram.sendMessage("High Temperature " + str(temp) + " C")

        if hum > 60:
            response_code = hologram.sendMessage("High Humidity " + str(hum) + " %")

    except (IOError, TypeError) as e:
        print(str(e))

    except KeyboardInterrupt as e:
        print(str(e))
        break

    # wait some time before re-updating the LCD
    sleep(0.5)