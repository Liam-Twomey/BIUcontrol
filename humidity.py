#!/usr/bin/env python3
# Must run "sudo pip3 install --install-option="--force-pi" Adafruit_DHT" on
# RPi before Adafruit_DHT library can be used.
# RPi before Adafruit_DHT library can be used.

import RPi.GPIO as GPIO
import time, threading
import argparse
import sys, select
import Adafruit_DHT
import BIUpinlist as pin

def checkconditions():
    hum, temp = Adafruit_DHT.read_retry(dht_sensor, pin.dht22)
    if hum is not None and temp is not None:
        return hum, temp
    else:
        return False

#Setup DHT
dht_sensor = Adafruit_DHT.DHT22
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Arguments for BIUhumidity.py')
    parser.add_argument('--opthum', help="optimize humidity to given value", required=True)
    args = parser.parse_args()
    targethum = args.opthum
    if type(targethum) is int:
        print('Targeting and maintaining %d %% humididty.').format(targethum)
        while True: # how to make this exit on plunge
            hum, temp  = checkconditions()
            if (hum < targethum):
                # make me work
                GPIO.output(pin.humpow,GPIO.HIGH)
                time.sleep(10)
                GPIO.output(pin.humpow,GPIO.LOW)
            #elif (hum > targethum):
            #    # make me work
            #    GPIO.output(pin.fan,GPIO.HIGH)
            else: pass
    elif targethum == False:
        print("Powering humidifier down.")
    else:
        print("Invalid argument to BIUhumidity.py")
        exit
        

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, pin.dht22)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")