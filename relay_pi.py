import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

try:
    i=0
    while (i<5):
        print i
        # Turn all relays OFF
        GPIO.output(3, GPIO.HIGH)

        # Sleep for 5 seconds
        sleep(2) 
        # Turn all relays ON
        GPIO.output(3, GPIO.LOW)
     
        # Sleep for 5 seconds
        sleep(2)
        i=i+1

finally:
    GPIO.output(3, GPIO.LOW)
    GPIO.cleanup()
    
