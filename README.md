# El primer *gateway* libre para IoT de Baleares
Este será el diario del desarrollo del primer LoRa gateway TTN de Baleares. Una plataforma gratuita de conectividad a internet de dispositivos IOT adscrita a la red TTN: [The Things Network](https://www.thethingsnetwork.org)
![Primer gateway TTN de Baleares](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/TTN_map_1st_balearic.png?raw=true)

## ¿Por qué LoRa?
Se alcanzan fácilmente 2km en área urbana y más de 10 km en área rural. Actualmente el récord tierra-tierra es de 210 km con una shield de Arduino de 16$ (febrero 2017) y globo-tierra 702 km (agosto 2017).
![LoRa](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LoRa-logo-transp-400x231-300x173.png?raw=true)

LoRa es una tecnología de transmisión inalámbrica, desarrollada entre 2008 y 2013 en Francia y adquirida y patentada por la compañía Semtech, que permite comunicar datos a muy larga distancia y con bajo consumo de energía (~100mW).

### ¿Por qué TTN?
![The Things Network](https://github.com/McOrts/LoRa_gateway/blob/master/pictures/ttn_logo.png?raw=true)

La vuelta de tuerca a esta solución de interconectividad de dispositivos la ha dado la red [The Things Network](https://www.thethingsnetwork.org). Que ha formado una comunidad abierta de *gateways* y nodos que permite la conectividad de dispositivos IoT sin 3G ni WiFi y sin coste. En realidad solo vamos a pagar el copywrite del chip LoRa de los dispositivos que compremos.

### Teoría de la señal
Estas comunicaciones utilizan las bandas ISM (Industrial Scientific & Medical) 868 MHz para Europa. Son de uso libre sin licencia pero limitadas a la potencia de 25 mW (p.r.a.) y tiempo de transmisión del 1% ([Orden IET/787/2013 del cuadro nacional de atribución de frecuencias](https://www.boe.es/buscar/act.php?id=BOE-A-2013-4845)). Como norma general, no envíes más de una vez cada 3 minutos y cumplirás la reglamentación. Si quieres enviar más a menudo, existen [calculadoras](https://docs.google.com/spreadsheets/d/1voGAtQAjC1qBmaVuP1ApNKs1ekgUjavHuVQIXyYSvNc/edit#gid=0) para obtener los tiempos entre envío mínimos. Para LoRaWAN, revisa la [Fair access policy](https://www.thethingsnetwork.org/forum/t/limitations-data-rate-packet-size-30-seconds-uplink-and-10-messages-downlink-per-day-fair-access-policy/1300).

<img src="https://github.com/McOrts/LoRa_gateway/blob/master/pictures/propagation.png" width="300" align="left" />)
__*Spreading Factor*__ es un importante cuando utilizamos un único canal de comunicación. El SF especifica la potencia de transmisión, la subfrecuencia y el tiempo de aire (Time on Air). En otras palabras, hace lo mismo que cuando conversamos en un entorno ruidoso, hablamos más despacio alargando las palabras. De esta manera un SF alto, 12 por ejemplo. Permite un mayor alcance pero menos capacidad de transmisión:

### La seguridad. ABP: Activation By Personalisation
En ABP un dispositivo no necesita los identificadores de DevEUI, ApEUI y AppKey. En cambio las claves de sesión, NwkSKey y AppSKey si, y las tiene preprogramadas el dispositivo, el cual ya estaría preregistrado en la red. Cuando el dispositivo se quiere comunicar, lo hace usando esas claves de sesión sin tener que usar ningún procedimiento de unión a la red.

# PRIMERA ITERACIÓN
## Un gateway SCGs ¡Mallorca ya está conectada a TTN!
SCG, ¨Single-channel gateways¨ no es la solución óptima para un Gateway de la red TTN pero permite realizar de forma rápida y barata una prueba de concepto que, de primeras, ya puede cubrir gran parte de una ciudad.

He utilizado la placa [TTGO LoRa32 V2.0 868 MHz](https://www.aliexpress.com/item/2-Pcs-TTGO-LORA32-V2-0-868-433Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card/32847443952.html). Basada en el microprocesador ESP32, con WiFi y BlueTooth. Además integra una pantallita Oled muy lograda y puede alimentarse con una LiPo y cargarla por USB, perfecta para desarrollar y hacer pruebas. !Y tan solo por 19€!
Para poner en marcha este *gateway* gracias a [@TCRobotics](https://twitter.com/TCRobotics) tenemos este manual https://bricolabs.cc/wiki/guias/lora_ttn que con unos conocimientos del IDE de Arduino, es fácil de seguir.

<img src="https://github.com/McOrts/LoRa_gateway/blob/master/pictures/LORA_TTN_Gateway_SCG.JPG" width="300" align="left" />)
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

Par la parte de configurar el nodo en TTN, Akirasan ha puesto en su web un buen tutoral [http://akirasan.net/nodo-lorawan-con-esp32/](http://akirasan.net/nodo-lorawan-con-esp32/).

# SEGUNDA ITERACIÓN
## Gateway multicanal con Resin
El dispositivo lo compré en AliExpres. Hay varias opciones en torno al hat RAK831 que usa el chipset SX1301. La distribución que he montado se desarrolló en un workshop del Things Network Conference 2018 utilizando una Raspberry Pi 3. En el aplicativo hay algunos aspectos en los que está verdes,, pero uno de los autores, [Jac  Kersing](https://www.thethingsnetwork.org/forum/u/kersing) está muy activo en los foros de TTN y me ha ayudado con algunos problemas. Y es el autor de la guía que he seguido para su montaje: https://www.thethingsnetwork.org/docs/gateways/rak831/

las caracteristicas del equipo son:
![Características del RAK831](https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/RAK831_characteristics.png?raw=true)

El dispositivo lo forma una placa LoRa, un placa GPS, un adaptador y una Raspberry Pi 3. La interconexión entre los módulos se puede seguir en este diagrama:
![RAK831 Diagrama de bloques](https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/RAK831_block_diagram.png?raw=true)

La aplicación es compleja. Corre en un tipo de contenedor facilitado por la plataforma [resin.io](http://resin.io) basado el código Python que debes descargar de un repositorio Git.
![Arquitectura resin.io](https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/resin.io_architecture.png?raw=true)

La operativa no se lleva desde una conexión directa a la Raspberry Pi, sino a una consola de resin:
![Consola resin.io](https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/resin.io_console.png?raw=true)


# TERCERA ITERACIÓN
## Gateway externo con el instalador Lorank8

<img src="https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/McOrts_TTN_gateway_RAK831_p2.jpg" width="300" align="right" />
La configuración anterior del gateway RAK831 basado en Raspberry Pi 3 presentaba problemas de estabilidad con errores recurrentes que me obligaban a reiniciar la aplicación Resin. Pero el mayor problema era la poca cobertura a pesar de utilizar la anterna de onda completa de RAK de 5.8dbi ya que tenía que estar en interior. La caja original no tiene ninguna estanqueidad. 

### La solución

Me he provisto de una de exterior con certificación IP67, la [Nebra de aluminio](https://www.ebay.co.uk/itm/223660547000). Así como de los prensa estopas necesarios para que los cables pasen al interior de la caja sin poner en peligro su estanqueidad. 
Es muy importante utilizar un cable de antena lo más corto posible. Por lo que lo más fácil es poner ambas en el mismo mástil. 
La antena de GPS queda en el interior con una cobertura reducida. Lo que no es un problema ya que la localizaciónd el gateway se configura manualmente.

Para instalar el software he seguido el documento del taller de Gateways de TTN Madrid de [@AngeLinuX99](https://github.com/AngeLinuX99).

### El problema de la temperatura. Monitorización 
Me preocupa que la falta de refrigeración activa lleve a la CPU de la Raspberry Pi a quemarse. Lo que no sabré si pasa hasta que lleguen los calores del verano. Preventivamente he reducido consumos innecesarios como la WiFi o el BlueTooth. Lo que se puede hacer fácilmente añadiendo al fichero de configuración /boot/config.txt los parámetros:
```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```

Y para conocer saber la temperatura he hecho un pequeño programa en Pyhton que basado en el comando vcgencmd lee el sensor del a CPU:
```
root@raspberrypi:~# vcgencmd measure_temp
temp=42.8'C
```
Transmite la medida a un Topic de MQTT y graba el valor en una tabla de una base de datos MySQL.
He completdo el programa con medidas de almacenamiento, carga de la CPU y memoria. De manera que tengo una información completa del estao de la Raspberry Pi que puedo mostrar en una aplicación Node-RED con el siguiente flujo:
<img src="https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/system_info_nodered-flow_RAK831.png" width="600" />
Finalmente tengo accesible el estado y evolución de estos indicadores en un dashboard de Node-RED que también me enviará alertas por mail cuando la aplicación deje de enviar mensajes al topic o la temperatura supere un umbral.
<img src="https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/RPI_RAK831_cpu_dashboard.png" width="250" align="right" />
Para ejecutar el programa he preferido hacerlo a través de una entrad en el cron del Raspbian:
```
# m h  dom mon dow   command
*/15 * * * * /usr/bin/python /home/pi/system_info_RAK831.py
```
### El resultado
El exfuerzo a dado buenos resultados. De momento he mapeado las zonas de costa con un nodo dado de alta en [TTN Mapper](https://ttnmapper.org/) con un alcance que ha superado los 10Km
<img src="https://github.com/McOrts/LoRa_gateway/blob/master/RAK831/McOrts_TTN_gateway_RAK831_TTN_mapper.png" />

__------- CONTINURÁ -------__


## Agradecimientos y referencias
* En primer lugar a __Alejandro Taracido__ alias [@TCRobotics](https://twitter.com/TCRobotics) fundador de [BricoLabs](https://twitter.com/Brico_Labs) por la base del código fuente del gatewawy basado en el repositorio de Jac Kersing https://github.com/kersing/ESP-1ch-Gateway-v5.0
* Para el nodo, __Jorge :P__ alias [akirasan](https://twitter.com/akirasan). Me ha guiado por el buen camino de código que el brillante programador Matthijs Kooijman ha dejado libre para todos nosotros https://github.com/matthijskooijman/arduino-lmic.
* A Ángel Luís Martínez [@AngeLinuX99](https://github.com/AngeLinuX99) por la práctica documentación del taller de Gateways de TTN Madrid. 
