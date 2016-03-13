#!/usr/bin/python

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED=23
START/STOP=24
LANE1=25
LANE2=22

def dptime ():
    waiting = 0
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setup(START/STOP, GPIO.IN)
    GPIO.setup(LANE1, GPIO.IN) # lane1
    GPIO.setup(LANE2, GPIO.IN) # lane2

    print "\nSTART YOUR ENGINES!"

    # wait for start button to be pressed
    while (GPIO.input(STAR) == GPIO.LOW):
        waiting += 1

    print "\nSOMETIMES YOU GOTTA RACE..."

    # start the race
    start = time.time()

    # turn light on
    GPIO.output(LED, GPIO.HIGH)

    # debounce the button hack
    time.sleep(1)

    # start main timer and watch for stop button
    done = 0
    lane1 = 0
    lane2 = 0
    lane3 = 0
    lane4 = 0

    while (done == 0):
       time.sleep(0.01)

       # stop button pressed
       if (GPIO.input(START/STOP) == GPIO.HIGH):
           done = time.time() - start
       else:
           # lane1 finished aka light blocked
           if (lane1 == 0 and GPIO.input(LANE1) == GPIO.LOW):
               lane1 = time.time() - start
               print "\nLANE1: " , '{0:.4g}'.format(lane1)

           # lane2 finished aka light blocked
           if (lane2 == 0 and GPIO.input(LANE2) == GPIO.LOW):
               lane2 = time.time() - start
               print "\nLANE2: " , '{0:.4g}'.format(lane2)

           # all lanes finished
           if (done == 0 and lane1 != 0 and lane2 != 0):
               done = time.time() - start

    # turn light off
    GPIO.output(LED, GPIO.LOW)
    print "\nDONE: " , '{0:.4g}'.format(done)

    # debounce start/stop button
    time.sleep(1)
    dptime()

dptime() 

GPIO.cleanup()
