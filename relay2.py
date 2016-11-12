import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

try:

    while (True):
        var = raw_input("1 to on 0 to off")
        print var
        if var is '1':
            print "ON"
            GPIO.output(3, GPIO.HIGH)
        elif var is '0':
            GPIO.output(3, GPIO.LOW)
        else:
            print "exit"
            break
        

        
finally:
    GPIO.output(3, GPIO.LOW)
    GPIO.cleanup()
    
