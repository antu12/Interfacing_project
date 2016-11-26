import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set up LED output
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(35, GPIO.OUT)
GPIO.output(35, GPIO.LOW)
# Callback function to run when motion detected
def motionSensor(channel):
    if GPIO.input(40):     # True = Rising
        GPIO.output(38, GPIO.HIGH)
    else:
        GPIO.output(38, GPIO.LOW)
    if GPIO.input(37):     # True = Rising
        GPIO.output(35, GPIO.HIGH)
    else:
        GPIO.output(35, GPIO.LOW)

# add event listener on pin 21
GPIO.add_event_detect(40, GPIO.BOTH, callback=motionSensor, bouncetime=300)

GPIO.add_event_detect(37, GPIO.BOTH, callback=motionSensor, bouncetime=300)

try:
    while True:
        time.sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."