import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(5, GPIO.OUT)
while True:
       i=GPIO.input(11)
       j=GPIO.input(12)
       #if i==0:                 #When output from motion sensor is LOW
            # print "No intruders",i
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(0.1)
       if i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             if j=1:
              i=0
              continue
             time.sleep(0.1)
       elif j==1:
               print "Intruder detected",j
             GPIO.output(5, 1)  #Turn ON LED
             if i=1:
              j=0
              continue
             time.sleep(0.1)
       if i==0:
              print "No intruders",i
             GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif j==0:
              print "No intruders",j
             GPIO.output(5, 0)  #Turn OFF LED
             time.sleep(0.1)
