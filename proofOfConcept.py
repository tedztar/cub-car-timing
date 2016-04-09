#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led=23
start=24
lane1=25
lane2=22

def dptime ():
    waiting = 0
    GPIO.setup(led, GPIO.OUT) # led
    GPIO.output(led, GPIO.LOW)
    GPIO.setup(start, GPIO.IN) # start gate / stop gate
    GPIO.setup(lane1, GPIO.IN) # lane1
    GPIO.setup(lane2, GPIO.IN) # lane2

    print "\nSTART YOUR ENGINES!"

    # wait for start button to be pressed
    while (GPIO.input(start) == GPIO.LOW):
        waiting += 1

    print "\nSOMETIMES YOU GOTTA RACE..."

    # start the race
    start = time.time()

    # turn light on
    GPIO.output(23, GPIO.HIGH)

    # debounce the button hack
    time.sleep(1)

    # start main timer and watch for stop button
    done = 0
    lane1Time = 0
    lane2Time = 0
    lane3Time = 0
    lane4Time = 0

    while (done == 0):
       time.sleep(0.01)

       # stop button pressed
       if (GPIO.input(start) == GPIO.HIGH):
           done = time.time() - start
       else:
           # lane1 finished aka light blocked
           if (lane1 == 0 and GPIO.input(lane1) == GPIO.LOW):
               lane1 = time.time() - start
               print "\nLANE1: " , '{0:.4g}'.format(lane1)

           # lane2 finished aka light blocked
           if (lane2 == 0 and GPIO.input(lane2) == GPIO.LOW):
               lane2 = time.time() - start
               print "\nLANE2: " , '{0:.4g}'.format(lane2)

           # all lanes finished
           if (done == 0 and lane1 != 0 and lane2 != 0):
               done = time.time() - start

    # turn light off
    GPIO.output(led, GPIO.LOW)
    print "\nDONE: " , '{0:.4g}'.format(done)
    
    print "/nLane1" + lane1Time
    print "/nLane2" + lane2Time
    # debounce start/stop button
    time.sleep(1)
    dptime()

dptime() 
GPIO.cleanup()
