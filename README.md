# El primer *gateway* libre para IoT de Baleares
Este será el diario del desarrollo del primer LoRa gateway TTN de Baleares. Una plataforma gratuita de conectividad a internet de dispositivos IOT abscrita a la red TTN: [The Thing Network](https://www.thethingsnetwork.org)
![Primer gateway TTN de Baleares](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/TTN_map_1st_balearic.png?raw=true)

## ¿Por qué LoRa?
Se alcanzan fácilmente 2km en área urbana y más de 10 km en área rural. ¡Actualmente el récord tierra-tierra es de 210 km con una shield de Arduino de 16$! (febrero 2017) y globo-tierra 702 km (agosto 2017).
![LoRa](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LoRa-logo-transp-400x231-300x173.png?raw=true)

LoRa es una tecnología de transmisión inalámbrica, desarrollada entre 2008 y 2013 en Francia y adquirida y patentada por la compañía Semtech, que permite comunicar datos a muy larga distancia y con bajo consumo de energía (~100mW).

### ¿Por qué TTN?
![The Thing Network](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/ttn_logo.png?raw=true)

La vuelta de tuerca a esta solución de interconectividad de dispositivos la ha dado la red [The Thing Network](https://www.thethingsnetwork.org). Que ha formado una comunidad abierta de *gateways* y nodos que permite la conectividad de dispositivos IoT sin 3G ni WiFi y sin coste. En realidad solo vamos a pagar el copywrite del chip LoRa de los dispositimos que compremos.

### Teoría de la señal
Estas comunicaciones utilizan las bandas ISM (Industrial Scientific & Medical) 868 MHz para Europa. Son de uso libre sin licencia pero limitadas a la potencia de 25 mW (p.r.a.) y tiempo de transmisión del 1% ([Orden IET/787/2013 del cuadro nacional de atribución de frecuencias](https://www.boe.es/buscar/act.php?id=BOE-A-2013-4845)). Como norma general, no envíes más de una vez cada 3 minutos y cumplirás la reglamentación. Si quieres enviar más a menudo, existen [calculadoras](https://docs.google.com/spreadsheets/d/1voGAtQAjC1qBmaVuP1ApNKs1ekgUjavHuVQIXyYSvNc/edit#gid=0) para obtener los tiempos entre envío mínimos. Para LoRaWAN, revisa la [Fair access policy](https://www.thethingsnetwork.org/forum/t/limitations-data-rate-packet-size-30-seconds-uplink-and-10-messages-downlink-per-day-fair-access-policy/1300).

__*Spreading Factor*__ es un importante cuando utilizamos un único canal de comunicación. El SF especifica la potencia de transmisión, la subfrecuencia y el tiempo de aire (Time on Air). En otras palabras, hace lo mismo que cuando conveersamos en un entorno ruidoso, hablamos más despacio alargando las palabras. De esta manera un SF alto, 12 por ejemplo. Permite un mayor alcance pero menos capacidad de transmisión:
![SF Propagacion](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/propagation.png?raw=true)

### La seguridad. ABP: Activation By Personalisation
En ABP un dispositivo no necesita los identificadores de DevEUI, ApEUI y AppKey. En cambio las claves de sesión, NwkSKey y AppSKey si, y las tiene preprogramadas el dispositivo, el cual ya estaría preregistrado en la red. Cuando el dispositivo se quiere comunicar, lo hace usando esas claves de sesión sin tener que usar ningún procedimiento de unión a la red.

# PRIMERA ITERACIÓN
## Un gateway SCGs ¡Mallorca ya está conectada a TTN!
SCG, ¨Single-channel gateways¨ no es la solución óptima para un Gateway de la red TTN pero permite realizar de forma rápida y barata una prueba de concepto que, de primeras, ya puede cubrir gran parte de una ciudad.

He utilizado la placa [TTGO LoRa32 V2.0 868 MHz](https://www.aliexpress.com/item/2-Pcs-TTGO-LORA32-V2-0-868-433Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card/32847443952.html). Basada en el microprocesador ESP32, con WiFi y BlueTooth. Además integra una pantallita Oled muy lograda y puede alimentarse con una LiPo y cargarla por USB, perfecta para desarrollar y hacer pruebas. !Y tan solo por 19€!
Para poner en marcha este *gateway* gracias a [@TCRobotics](https://twitter.com/TCRobotics) tenemos este manual https://bricolabs.cc/wiki/guias/lora_ttn que con unos conocimientos del IDE de Arduino, es fácil de seguir.

![SF Propagacion](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LORA_TTN_Gateway_SCG.JPG?raw=true)
El resultado a sido un sencillo dispositivo en el identificado eui-d8a01dffff402024 que he conectado a la antena WiFi de mi mástil de comunicaciones. En el que tengo una antena de 868,600 MHz pero que por alguna razón, tiene un corto con la masa. El Spreading Factor que he configurado es de 7 pendiente de hacer pruebas de alcance. Se puede consultar el estado y localización en: https://www.thethingsnetwork.org/u/mcorts

![Antenna](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/antennas_mast.png)

En una de las Raspberry Pi de mi domótica he dejado arrrancada la consola de tráfico del Gateway. Y sorpresa: !tengo conexiones de dispositivos! Pero si yo no he montado todavia mi nodo y en Mallorca no hay ningún Gateway de TTN. Espero resolver algún día este misterio.

![TTN Consola](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/TTN_Consola_RBPy.png?raw=true)

## Y ahora el nodo. Un microcontrolador con sensor de movimiento
![TTN Consola](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LORA_TTN_Node_MovementSensor.GIF?raw=true)

Aprovechando el otro [TTGO LoRa32 V2.0 868 MHz](https://www.aliexpress.com/item/2-Pcs-TTGO-LORA32-V2-0-868-433Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card/32847443952.html) le conecté el sensor ADXL345. Y con una profunda reprogramación basada en estas librerías he podido hacerlo vivir:
- librería de Adafruit para el sensor de movimiento [ADXL345](https://github.com/adafruit/Adafruit_ADXL345)
- Librería de Adafruit para pantallas OLED [SSD1306](https://github.com/adafruit/Adafruit_SSD1306)
- Codigo para [nodo TTN sobre ESP32](https://github.com/matthijskooijman/arduino-lmic)

![ESP32 conectividad con ADXL345](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/lolin32-and-adxl345_bb.png?raw=true)

El ADXL345 es un sensor muy versátil y preciso. No solo nos dice su posición respecto a las tres coordenadas del espacio. Si no que nos determina la aceleración en m/s2. 
![ADXL345](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/ADXL345.jpg?raw=true)

# SEGUNDA ITERACIÓN
Ya estoy preparando un potente Gateway multicanal. Y la tarea de reparar la antena de 868Mhz. Por el camino a tenerlo todo operativo, espero convencer a un par de empresas a que empiecen a comunicar sus dispositivos por mi gateway actual.

__------- CONTINURÁ -------__


## Agradecimientos y referencias
- En primer lugar a __Alejandro Taracido__ alias [@TCRobotics](https://twitter.com/TCRobotics) fundador de [BricoLabs](https://twitter.com/Brico_Labs) por la base del código fuente del gatewawy basado en el repositorio de Jac Kersing https://github.com/kersing/ESP-1ch-Gateway-v5.0
- Para el nodo, __Jorge :P__ alias [akirasan](https://twitter.com/akirasan). Me ha guiado por el buen camino de código que el brillante programador Matthijs Kooijman ha dejado libre para todos nosotros https://github.com/matthijskooijman/arduino-lmic.
