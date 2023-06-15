# Remote-Monitoring-with-Cellular-IoT
These are the instructions on how to build a Temperature and Humidity and Motion detection device with GrovePi and Hologram Nova. 

Scroll down for the instructions on how to build the motion detection device. 

Here are the instructions for setting up the Raspberry Pi for both projects. 

Things used in this project:

Hardware components:

Raspberry Pi Zero WH, GrovePi Zero ,Grove-Temperature and Humidity Sensor, Grove LCD RGB Backlight, Hologram SIM

Software Apps:

GrovePi, Python, Hologram CLI

GrovePi Zero is a HAT from Dexter Industries  that allows Grove PIR motion sensor to connect to Raspberry Pi zero with out needing soldering or breadboards. One can plug in the Grove water sensor start programming.

Grove Temperature and Humidity sensor works with digital I/O pins and it can be connected to D3 port Grove Pi Zero as shown below.
The installation instructions for Grove Pi Zero and Hologram SIM are as follows:


1.) Download the latest version of Raspibian from the Raspberry pi download link. Install the Raspberry Pi image on a SD card using instructions provided in their installation guide at https://www.raspberrypi.com/documentation/computers/getting-started.html.

2.) Install Grove Pi software and reboot using following commands:
     
`sudo curl -kL dexterindustries.com/update_grovepi|bash`
`sudo reboot`

3. Grove Firmware Update

Run the firmware update without any sensors or HDMI connected to the pi. Run the following commands to update the firmware:

`cd /home/pi/Dexter/GrovePi/Firmware`
`sudo bash firmware_update.sh`

Then next, let’s reinstall the GrovePi dependencies (there might be something that’s still not set up). After you update the firmware, you’ll reboot it. So, open a terminal and follow this commands:

`cd /home/pi/Dexter/GrovePi/Script
sudo bash install.sh
sudo reboot`


4.) Get a Hologram SIM and register it at the Hologram portal.

<img width="299" alt="Screen Shot 2023-06-15 at 5 12 31 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/49957de4-78ca-4c96-9a8b-ca0d9fb5d119">

  5.) Lastly, follow the Hologram's documentation to install Hologram's Command Line Interface (CLI) and test the connectivity as shown in the documentation. Hologram CLI and Python SDK can be installed using a curl command as shown below :

 `curl -L hologram.io/python-install | bash`

 Update to a latest version:
   `curl -L hologram.io/python-update | bash`

 Check signal strength:
     `sudo hologram modem signal`

 Send a sample data message:
     `sudo hologram send "Hello World"`
     
**Temperature and Humidity Detection Device**

A Temperature and Humidity Grove sensor is used in this project to measure relative humidity and temperature. It provides relative humidity measurement expressed as a percentage of the ration of moisture in the air to the maximum amount that can be held in the air at that temperature. The relative humidity changes with temperature as air becomes hotter and it holds more moisture.

Now, we can move back to the temperature and humidity monitoring. The following program (temphumidity_sensor_led.py) checks the temperature and humidity sensor output sets the text on LCD.
<img width="620" alt="Screen Shot 2023-06-14 at 11 57 13 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/71bf82cf-8ac4-4747-a74c-f597376d69f9">


First  a cellular connection is established using the credentials that uses a devicekey obtained from Hologram dashboard. 

<img width="476" alt="Screen Shot 2023-06-15 at 4 57 23 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/1d41e63a-739f-4b9d-8657-62a92db71801">


After execution of the above program, the status is displayed on the LCD as shown in the picture.

 To run the file on the raspberry pi, run `$ sudo python temp_humidity.py`



After reading the digital input from port D3 it displays the sensor value on the LCD and it also sends notification using cellular network if the sensor value  for temperature or humidity exceeds the predefined threshold values.
<img width="637" alt="Screen Shot 2023-06-14 at 11 58 32 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/16eb351e-85a7-4585-8193-1a39cfc3a5cd">


Configure routes in Hologram dash board to send the notifications (e.g., SMS, email etc).
<img width="652" alt="Screen Shot 2023-06-14 at 11 58 43 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/b717dd00-f9de-43e8-bf13-9005ad62545f">

**Motion Detection Device**

This project uses the Grove Motion Sensor that can be used to detect movement of people, animals or other objects. It also can send notifications using cellular network.

Things used in this project:

Hardware components:

Raspberry Pi Zero WH, GrovePi Zero ,Grove-Temperature and Humidity Sensor, Grove LCD RGB Backlight, Hologram SIM

Software Apps:

GrovePi, Python, Hologram CLI

Grove - Adjustable PIR Motion Sensor - It uses passive infrared  motion sensor, which can detect infrared object motion up to 3 meters. It is an electronic sensor that measures infrared (IR) light radiating from objects in its field of view. 

Animals, people or various objects emit heat energy in the form of radiation. This radiation is not visibile to human eye as it radiates at infrared wavelengths, but it can be detected PIR-based motion detector. These are commonly used in burglar alarms.

<img width="472" alt="Screen Shot 2023-06-15 at 4 50 20 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/94ace4a3-4ddd-4bd1-8ef5-b0a038b56e3a">

The following program (motion_sensor_led.py) checks the water sensor output sets the text on LCD.
After execution of the above program, the status is displayed on the LCD.

` $ sudo python motion_sensor_led.py`

First  a cellular connection is established using the credentials that uses a devicekey obtained from Hologram dashboard.
<img width="455" alt="Screen Shot 2023-06-15 at 4 50 40 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/5104cf6f-b6e3-42bc-a5b9-99ec3e7c7975">

After reading the digital input from port D3 it determines if motion is detected and displays the message on the LCD and it also sends notification using cellular network if there is a movement.

Configure routes in Hologram dash board to send the notifications (e.g., SMS, email etc).

<img width="633" alt="Screen Shot 2023-06-15 at 4 50 58 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/493d4aa4-2b06-4135-9b9a-280b4e7cf67b">

<img width="641" alt="Screen Shot 2023-06-15 at 4 51 04 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/a69e8e34-38d5-4b82-b0f7-55fa43666ab2">
