# LoRa_gateway
Diario del desarrollo del primer LoRa gateway TTN de Baleares. Una nueva plataforma gratuita de conectividad a internet de dispositivos IOT abscrita a la red TTN: The Thing Network.

## ¿LoRa?
### Fundamentos

### Teoría de la señal

*spreading factor* es importante cuando utilizamos un único canal de comunicación. El spreading factor especifica la potencia de transmisión, la subfrecuencia y el tiempo de aire (Time on Air).
[https://github.com/McOrts/LoRa_gateway/blob/master/pictures/propagation.png?raw=true]

## Un gateway SCGs. Primera iteracción
SCG, ¨Single-channel gateways¨ no es la solución óptima para un Gateway de la red TTN pero permite realizar de forma rápida y barata una prueba de concepto que, de primeras, ya puede cubrir gran parte de una ciudad.
He utilizado la placa TTGO LoRa32 V2.0 868 MHz. Basada en el microprocesador ESP32, con WiFi integran una pantallita Oled muy lograda y pueden alimentarse con una LiPo y cargarla por USB, perfecta para desarrollar y hacer pruebas.
Meta-instrucciones: https://bricolabs.cc/wiki/guias/lora_ttn

## Un nodo ESP32. Sensor de movimiento.
Código basado en:
librería de Adafruit para el ADXL345
Librería para pantallas OLED 
Codigo para nodo TTN sobre ESP32 https://github.com/matthijskooijman/arduino-lmic



Agradecimientos:
En primer lugar a Alejandro Taracido alias @TCRobotics https://twitter.com/TCRobotics fundador de https://twitter.com/Brico_Labs por la base del código fuente del gatewawy basado en el repositorio de Jac Kersing https://github.com/kersing/ESP-1ch-Gateway-v5.0.
En el nodo, Jorge :P (akirasan) https://twitter.com/akirasan. Me ha guiado por el buen camino de código que el brillante programador Matthijs Kooijman ha dejado libre para todos nosotros https://github.com/matthijskooijman/arduino-lmic.
