#!/usr/bin/env python3
# Must run "sudo pip3 install --install-option="--force-pi" Adafruit_DHT" on
# RPi before Adafruit_DHT library can be used.

# Uncomment for use of pi
import RPi.GPIO as GPIO
import time, threading
import argparse
import sys, select
import BIUpinlist as pin

def filterforward(filterposition):
    print("Advancing the filter")
    GPIO.output(filterposition,GPIO.HIGH)

def powerupsensors(sensorpower):
    GPIO.output(sensorpower,GPIO.HIGH)

def powerdownsensors(sensorpower):
    GPIO.output(sensorpower,GPIO.LOW)
    
def filterreverse(filterposition,filterreversedelay):
    time.sleep(filterreversedelay)
    print("Reversing the filter")
    GPIO.output(filterposition,GPIO.LOW)
def checkconditions():
    hum, temp = Adafruit_DHT.read_retry(dht_sensor, pin.dht22)
    if hum is not None and temp is not None:
        return hum, temp
    else:
        return False

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Arguments for BIUpowerupdown')
    parser.add_argument('--updown', help='Power up or down',required=True)
    args = parser.parse_args()
    dht_sensor = Adafruit_DHT.DHT22

    GPIO.setwarnings(False)
    GPIO.cleanup()    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin.filterposition,GPIO.OUT)
    GPIO.setup(pin.sensorpower,GPIO.OUT)
    GPIO.setup(pin.sensorpower,GPIO.OUT)
    GPIO.setup(pin.pedalsensor,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(pin.interlock,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    if args.updown == 'up':
        # Power up sensors and check interlock
        powerupsensors(pin.sensorpower)
        '''if GPIO.input(pin.interlock)==1:
            print("Interlock fail: cryogen container is not in place")
            powerdownsensors(pin.sensorpower)
            filterreverse(pin.filterposition,0)
            exit()
        else:
            print("Safety interlock pass: cryogen container is in place")
            # put filter into place and wait'''
        filterforward(pin.filterposition)
    elif args.updown == 'down':
        powerdownsensors(pin.sensorpower)
        filterreverse(pin.filterposition,0)
    print("Done!")

