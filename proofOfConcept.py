#!/usr/bin/python

import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def dptime ():
    waiting = 0
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.LOW)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(25, GPIO.IN) # lane1
    GPIO.setup(22, GPIO.IN) # lane2

    print "\nSTART YOUR ENGINES!"

    # wait for start button to be pressed
    while (GPIO.input(24) == GPIO.LOW):
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
    lane1 = 0
    lane2 = 0
    lane3 = 0
    lane4 = 0

    while (done == 0):
       time.sleep(0.01)

       # stop button pressed
       if (GPIO.input(24) == GPIO.HIGH):
           done = time.time() - start
       else:
           # lane1 finished aka light blocked
           if (lane1 == 0 and GPIO.input(25) == GPIO.LOW):
               lane1 = time.time() - start
               print "\nLANE1: " , '{0:.4g}'.format(lane1)

           # lane2 finished aka light blocked
           if (lane2 == 0 and GPIO.input(22) == GPIO.LOW):
               lane2 = time.time() - start
               print "\nLANE2: " , '{0:.4g}'.format(lane2)

           # all lanes finished
           if (done == 0 and lane1 != 0 and lane2 != 0):
               done = time.time() - start

    # turn light off
    GPIO.output(23, GPIO.LOW)
    print "\nDONE: " , '{0:.4g}'.format(done)

    # debounce start/stop button
    time.sleep(1)
    dptime()

dptime() 

