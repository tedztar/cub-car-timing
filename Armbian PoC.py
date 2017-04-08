import wringpi
import time

INPUT = 0
OUTPUT = 1
LOW = 0
HIGH = 1
BUTTONS = [13,12,10,11]
LEDS = [0,1,2,3,4,5,6,7,8,9]
PUD_UP = 2
DEBUG = 1

#use for the gpio pins, no pins set
led=0
start=0
lane1=0
lane2=0
lane3=0
lane4=0
lane5=0
lane6=0
#DO NOT CHANGE!!!!!!! USED FOR SETING UP THE GPIO PINS
BUTTONS = [start, lane1, lane2, lane3, lane4, lane5, lane6]

for button in BUTTONS:
  wiringpi.pinMode(button,Input)
  wiringpi.pullUpDnControll(button,PUD_UP)

#set up the led
wiringpi.pinMode(led, OUTPUT)

waiting = 0
GPIO.setup(led, GPIO.OUT) # led
GPIO.output(led, GPIO.LOW)
GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP) # start gate / stop gate
GPIO.setup(lane1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane1
GPIO.setup(lane2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane2
GPIO.setup(lane3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane2
GPIO.setup(lane4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane2
GPIO.setup(lane5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane2
GPIO.setup(lane6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # lane2

print ("start your engins")

# wait for start button to be pressed
while (GPIO.input(start) == GPIO.LOW):
    waiting += 1

print ("\nSOMETIMES YOU GOTTA RACE...")

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
lane5Time = 0
lane6Time = 0

while (done == 0):
    time.sleep(0.01)

    # stop button pressed
    if (GPIO.input(start) == GPIO.HIGH):
        done = time.time() - start
    else:
           # lane1 finished aka light blocked
        if (lane1Time == 0 and GPIO.input(lane1) == GPIO.LOW):
            lane1Time = time.time() - start
            print ("\nLANE1: ") , '{0:.4g}'.format(lane1Time)

           # lane2 finished aka light blocked
        if (lane2Time == 0 and GPIO.input(lane2) == GPIO.LOW):
            lane2Time = time.time() - start
            print ("\nLANE2: ") , '{0:.4g}'.format(lane2Time)

           # lane3 finished aka light blocked
        if (lane3Time == 0 and GPIO.input(lane3) == GPIO.LOW):
            lane3Time = time.time() - start
            print ("\nLANE2: ") , '{0:.4g}'.format(lane3Time)
              
           # lane4 finished aka light blocked
        if (lane4Time == 0 and GPIO.input(lane4) == GPIO.LOW):
            lane4Time = time.time() - start
            print ("\nLANE2: ") , '{0:.4g}'.format(lane4Time)

           # lane5 finished aka light blocked
        if (lane5Time == 0 and GPIO.input(lane5) == GPIO.LOW):
            lane5Time = time.time() - start
            print ("\nLANE2: ") , '{0:.4g}'.format(lane5Time)

           # lane6 finished aka light blocked
        if (lane6Time == 0 and GPIO.input(lane6) == GPIO.LOW):
            lane6Time = time.time() - start
            print ("\nLANE2: ") , '{0:.4g}'.format(lane6Time)
        

           # all lanes finished
        if (done == 0 and lane1 != 0 and lane2 != 0 and lane3 != 0 and lane4 != 0 and lane5 != 0 and lane6 != 0):
            done = time.time() - start

# turn light off
GPIO.output(led, GPIO.LOW)
print ("\nDONE: ") , '{0:.4g}'.format(done)
    
print ("/nLane1") + lane1Time
print ("/nLane2") + lane2Time
# debounce start/stop button
time.sleep(1)

GPIO.cleanup()
