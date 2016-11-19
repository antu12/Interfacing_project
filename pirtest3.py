import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.IN) #Read output from PIR motion sensor 
GPIO.setup(3, GPIO.OUT) #LED output pin 
GPIO.setup(12, GPIO.IN) #Read output from PIR motion sensor 
GPIO.setup(19, GPIO.OUT) 
GPIO.output(3, 0) 
GPIO.output(19, 0) 
while True:
       i=GPIO.input(11)
       j=GPIO.input(12)
       if i==0:
             print "Red No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.5)
       if j==0:
             print "Green No intruders",j
             GPIO.output(19, 0)  #Turn OFF LED
             time.sleep(0.5)

       if j==1:               #When output from motion sensor is HIGH
             print "Green Intruder detected",j
             
	     GPIO.output(19, 1)  #Turn ON LED
	     time.sleep(0.5)
       if i==1:
             print "Red Intruder detected",i
             GPIO.output(3, 1) #Turn ON LED
	     time.sleep(0.5)
