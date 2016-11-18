import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(5, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(12)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(5, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(5, 1)  #Turn ON LED
             time.sleep(0.1)
