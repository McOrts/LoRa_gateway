# LoRa_gateway
Diario del desarrollo del primer LoRa gateway TTN de Baleares. Una nueva plataforma gratuita de conectividad a internet de dispositivos IOT abscrita a la red TTN: The Thing Network.

## ¿LoRa?
### Fundamentos

### Teoría de la señal

*spreading factor* es importante cuando utilizamos un único canal de comunicación. El spreading factor especifica la potencia de transmisión, la subfrecuencia y el tiempo de aire (Time on Air).
[https://github.com/McOrts/LoRa_gateway/blob/master/pictures/propagation.png?raw=true]

## SCGs Primera iteracción
SCG, ¨Single-channel gateways¨ no es la solución óptima para un Gateway de la red TTN pero permite realizar de forma rápida y barata una prueba de concepto que, de primeras, ya puede cubrir gran parte de una ciudad.
He utilizado la placa TTGO LoRa32 V2.0 868 MHz. Basada en el microprocesador ESP32, con WiFi integran una pantallita Oled muy lograda y pueden alimentarse con una LiPo y cargarla por USB, perfecta para desarrollar y hacer pruebas.
Meta-instrucciones: https://bricolabs.cc/wiki/guias/lora_ttn
