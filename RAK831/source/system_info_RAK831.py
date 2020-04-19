#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
#import MySQLdb as mdb
import json
import logging
import paho.mqtt.client as mqtt
from pprint import pprint

# Then the code sets up the logging module. We are going to use the basicConfig() function to set up the default handler 
# so that any debug messages are written to the file /home/pi/event_error.log.
logging.basicConfig(filename='/home/pi/system_info_RAK831.log',
  level=logging.DEBUG,
  format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# Read the configuration file
DEFAULT_CONFIG_PATH = '/home/pi/config.json'
with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
  config = json.load(config_file)

# Function for storing readings into MySQL
def insertDB(system_load, ram, disk, temperature):
  try:
    con = mdb.connect(config['db_server_ip'],
                      config['db_update_user'],
                      config['db_update_password'],
                      'measurements');
    cursor = con.cursor()

    sql = "INSERT INTO system_info_RAK831(`load`,`ram`,`disk`,`temperature`) \
    VALUES ('%s', '%s', '%s', '%s')" % \
    (system_load, ram, disk, temperature)
    cursor.execute(sql)
    con.commit()
    con.close()
  except mdb.Error, e:
    con.rollback()
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

# returns the system load over the past minute
def get_load():
    try:
        s = subprocess.check_output(["cat","/proc/loadavg"])
        return float(s.split()[0])
    except:
        return 0

# Returns the used ram as a percentage of the total available
def get_ram():
    try:
        s = subprocess.check_output(["free","-m"])
        lines = s.split("\n")
        used_mem = float(lines[1].split()[2])
        total_mem = float(lines[1].split()[1])
        return (int((used_mem/total_mem)*100))
    except:
        return 0

# Returns the percentage used disk space on the /dev/root partition
def get_disk():
    try:
        s = subprocess.check_output(["df","/"])
        lines = s.split("\n")
        return int(lines[1].split("%")[0].split()[4])
    except:
        return 0

# Returns the temperature in degrees C of the CPU
def get_temperature():
    try:
        dir_path="/opt/vc/bin/vcgencmd"
        s = subprocess.check_output([dir_path,"measure_temp"])
        return float(s.split("=")[1][:-3])
    except:
        return 0

# Function for publish MQTT messages
def publish_MQTT_messages (p_disk,p_subtopic):
  try:
    client = mqtt.Client()
    # compose the message
    topic = config['rak831']['topic'] + '/' + p_subtopic
    #xpayload = '{:3.2f}'.format(p_disk / 1.)
    payload =  p_disk
    print ("Publishing " + payload + " to topic: " + topic + " ...")
    client.connect(config['MQTT']['broker_server_ip'],1883,60)
    client.publish (topic, payload)

    client.disconnect();
  except Exception as e:
    print ("exception")
    logger.error("Exception MQTT sending message: %s\n"+" "+e.__str__())

got_load = str(get_load())
got_ram = str(get_ram())
got_disk = str(get_disk())
got_temperature = str(get_temperature())
publish_MQTT_messages(got_load, 'load')
publish_MQTT_messages(got_ram, 'ram')
publish_MQTT_messages(got_disk, 'disk')
publish_MQTT_messages(got_temperature, 'temperature')

#insertDB(got_load, got_ram, got_disk, got_temperature)

