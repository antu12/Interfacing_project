import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.IN) #Read output from PIR motion sensor 
GPIO.setup(3, GPIO.OUT) #LED output pin 
GPIO.setup(12, GPIO.IN) #Read output from PIR motion sensor 
GPIO.setup(5, GPIO.OUT) 
GPIO.output(3, 0) 
GPIO.output(5, 0) 
while True:
       i=GPIO.input(11)
       j=GPIO.input(12)
       #if i==0:                 #When output from motion sensor is LOW
            # print "No intruders",i
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(0.1)
       if i==0:
             print "White No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif j==0:
             print "Red No intruders",j
             GPIO.output(5, 0)  #Turn OFF LED
             time.sleep(0.1)

       if j==1:               #When output from motion sensor is HIGH
             print "Red Intruder detected",j
             if i==1:
                j=0
#               GPIO.output(3, 0)
                continue
		GPIO.output(5, 1)  #Turn ON LED
	        time.sleep(0.1)
       if i==1:
             print "White Intruder detected",i
	     if j==1:
                i=0
#              GPIO.output(5, 0)
                continue
             GPIO.output(3, 1) #Turn ON LED
	     time.sleep(0.1)
