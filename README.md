# Remote-Monitoring-with-Cellular-IoT
Temperature and Humidity Monitoring Project with GrovePi and Hologram Nova
A Temperature and Humidity Grove sensor is used in this project to measure relative humidity and temperature. It provides relative humidity measurement expressed as a percentage of the ration of moisture in the air to the maximum amount that can be held in the air at that temperature. The relative humidity changes with temperature as air becomes hotter and it holds more moisture.


Things used in this project:

Hardware components:
Raspberry Pi Zero  WH
GrovePi Zero 
Grove-Temperature and Humidity Sensor
Grove LCD RGB Backlight
Hologram SIM

Software Apps:
GrovePi 
Python
Hologram CLI

GrovePi Zero is a HAT from Dexter Industries  that allows Grove PIR motion sensor to connect to Raspberry Pi zero with out needing soldering or breadboards. One can plug in the Grove water sensor start programming.

Grove Temperature and Humidity sensor works with digital I/O pins and it can be connected to D3 port Grove Pi Zero as shown below.
The installation instructions for Grove Pi zero and Hologram SIM are provided here .



The following program (temphumidity_sensor_led.py) checks the temperature and humidity sensor output sets the text on LCD.

First  a cellular connection is established using the credentials that uses a devicekey obtained from Hologram dashboard. 



After execution of the above program, the status is displayed on the LCD as shown in the picture.

 $ sudo python temphumidity_sensor_led.py



After reading the digital input from port D3 it displays the sensor value on the LCD and it also sends notification using cellular network if the sensor value  for temperature or humidity exceeds the predefined threshold values.

Configure routes in Hologram dash board to send the notifications (e.g., SMS, email etc).



