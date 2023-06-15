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

<img width="639" alt="Screen Shot 2023-06-15 at 5 15 13 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/434aa10e-fa47-407e-9dd3-748cb793cdab">


First  a cellular connection is established using the credentials that uses a devicekey obtained from Hologram dashboard. 

<img width="476" alt="Screen Shot 2023-06-15 at 5 15 58 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/e1568409-9370-460e-a18c-87d899d52996">

After execution of the above program, the status is displayed on the LCD as shown in the picture.

 To run the file on the raspberry pi, run `$ sudo python temp_humidity.py`



After reading the digital input from port D3 it displays the sensor value on the LCD and it also sends notification using cellular network if the sensor value  for temperature or humidity exceeds the predefined threshold values.

<img width="642" alt="Screen Shot 2023-06-15 at 5 16 13 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/75c7d6b7-36b5-4a99-b447-494443c1eab9">


Configure routes in Hologram dash board to send the notifications (e.g., SMS, email etc).

<img width="650" alt="Screen Shot 2023-06-15 at 5 16 28 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/0bee4c77-dbae-45f9-b5c6-4e950de3c1bf">

**Motion Detection Device**

This project uses the Grove Motion Sensor that can be used to detect movement of people, animals or other objects. It also can send notifications using cellular network.

Things used in this project:

Hardware components:

Raspberry Pi Zero WH, GrovePi Zero ,Grove-Temperature and Humidity Sensor, Grove LCD RGB Backlight, Hologram SIM

Software Apps:

GrovePi, Python, Hologram CLI

Grove - Adjustable PIR Motion Sensor - It uses passive infrared  motion sensor, which can detect infrared object motion up to 3 meters. It is an electronic sensor that measures infrared (IR) light radiating from objects in its field of view. 

Animals, people or various objects emit heat energy in the form of radiation. This radiation is not visibile to human eye as it radiates at infrared wavelengths, but it can be detected PIR-based motion detector. These are commonly used in burglar alarms.

<img width="362" alt="Screen Shot 2023-06-15 at 5 16 45 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/21a50320-8f0f-4f37-acbe-21b807424b74">

The following program (motion_sensor_led.py) checks the water sensor output sets the text on LCD.
After execution of the above program, the status is displayed on the LCD.

` $ sudo python motion_sensor_led.py`

First  a cellular connection is established using the credentials that uses a devicekey obtained from Hologram dashboard.

<img width="394" alt="Screen Shot 2023-06-15 at 5 17 00 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/24820979-a4ae-4468-9f0d-93d31b5f7127">

After reading the digital input from port D3 it determines if motion is detected and displays the message on the LCD and it also sends notification using cellular network if there is a movement.

Configure routes in Hologram dash board to send the notifications (e.g., SMS, email etc).

<img width="642" alt="Screen Shot 2023-06-15 at 5 17 12 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/547b8138-3631-46a9-b7ad-15316359a121">

<img width="687" alt="Screen Shot 2023-06-15 at 5 17 19 PM" src="https://github.com/arunjo5/Remote-Monitoring-with-Cellular-IoT/assets/136642643/27b3f25d-8bb2-4e9b-8e0d-8a1ae407a006">
