# Movement sensor portable device connected with LoRa to TTN
It is a portable device that sends a signal every time it moves. It uses the free LoRaWAN network that through [The Thing Network](https://www.thethingsnetwork.org) allows internet access to your datas.

![TTN Consola](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LORA_TTN_Node_MovementSensor.GIF?raw=true)

## Why LoRa?
It is easily reached 2km in urban area and more than 10km in rural area. Currently, the land-to-land record is 210 km with an Arduino shield of $ 16 (February 2017) and baloon-to-land of 702 km (August 2017).

![LoRa](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LoRa-logo-transp-400x231-300x173.png?raw=true)

LoRa is a wireless transmission technology, developed between 2008 and 2013 in France and acquired and patented by the company Semtech, which allows to communicate data over a long distance and with low power consumption (~ 100mW).

The __spreading factor__ is the most important parameter to set in LoRa networks. It specifies the speed/datarate in which the gateway and node communicate. 

![SF Propagacion](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/propagation.png?raw=true)

## Why TTN?
![The Thing Network](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/ttn_logo.png?raw=true)

The final twist of the screw to this solution of interconnection of devices was made by the network [The Thing Network](https://www.thethingsnetwork.org). That has build an open community of *gateways* and nodes that allows the connectivity of IoT devices without 3G or WiFi and free of charges. Actually we are only need to pay for the copywrite of the LoRa chip of the devices that we buy.

# Hands on
I used the microcontroler [TTGO LoRa32 V2.0 868 MHz](https://www.aliexpress.com/item/2-Pcs-TTGO-LORA32-V2-0-868-433Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card/32847443952.html) that attached to the movement sensor ADXL345.

![ADXL345](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/ADXL345.jpg?raw=true)

The ADXL345 is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16g. Digital output data is formatted as 16-bit twos complement and is accessible through either a SPI (3- or 4-wire) or I2C digital interface.
The ADXL345 is well suited for mobile device applications. It measures the static acceleration of gravity in tilt-sensing applications, as well as dynamic acceleration resulting from motion or shock. Its high resolution (4 mg/LSB) enables measurement of inclination changes less than 1.0°.

Several special sensing functions are provided. Activity and inactivity sensing detect the presence or lack of motion and if the acceleration on any axis exceeds a user-set level. Tap sensing detects single and double taps. Free-fall sensing detects if the device is falling. These functions can be mapped to one of two interrupt output pins. An integrated, patent pending 32-level first in, first out (FIFO) buffer can be used to store data to minimize host processor intervention.

## Connection and layout
I used the following connection from the module above to my Wemos Mini

TTGO LoRa32 Connection	- Module Connection
3v3	    - VCC
Gnd	    - Gnd
SDA 21	 - SDA
SCL 22	 - SCL

![ESP32 conectividad con ADXL345](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/lolin32-and-adxl345_bb.png?raw=true)

The program is based on these libraries:
- Library of Adafruit for [ADXL345](https://github.com/adafruit/Adafruit_ADXL345)
- Library of Adafruit for OLED screen [SSD1306](https://github.com/adafruit/Adafruit_SSD1306)
- Code for [TTN node for ESP32](https://github.com/matthijskooijman/arduino-lmic)
