import time
import RPi.GPIO as GPIO
import mysql.connector

GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering

conn=mysql.connector.connect(user='root', password='Nopassword01', host='172.16.34.81', database='autohome')
# Set up input pin
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pir 1
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pir 2
# Set up LED output
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)

GPIO.setup(35, GPIO.OUT)
GPIO.output(35, GPIO.LOW)
# Set relay pins as output
GPIO.setup(11, GPIO.OUT) #Light 1
GPIO.output(11, GPIO.LOW)

GPIO.setup(13, GPIO.OUT) #Light 2
GPIO.output(13, GPIO.LOW)



# Callback function to run when motion detected
def motionSensor(channel):
    if GPIO.input(40):     # True = Rising
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH) #Turn Light 1 On
        str_query = "UPDATE `switch` SET `sw_1` = '1' WHERE `switch`.`id_switch` = 'room1'"
	cursor=conn.cursor()
	cursor.execute(str_query)
	conn.commit()
    else:
        GPIO.output(38, GPIO.LOW)
        GPIO.output(11, GPIO.LOW) #Turn Light 1 Off
        str_query = "UPDATE `switch` SET `sw_1` = '0' WHERE `switch`.`id_switch` = 'room1'"
	cursor=conn.cursor()
	cursor.execute(str_query)
	conn.commit()
	
    if GPIO.input(37):     # True = Rising
        GPIO.output(35, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH) #Turn Light 2 On
        str_query = "UPDATE `switch` SET `sw_2` = '1' WHERE `switch`.`id_switch` = 'room1'"
	cursor=conn.cursor()
	cursor.execute(str_query)
	conn.commit()
    
    else:
        GPIO.output(35, GPIO.LOW)
        GPIO.output(13, GPIO.LOW) #Turn Light 2 Off
        str_query = "UPDATE `switch` SET `sw_2` = '0' WHERE `switch`.`id_switch` = 'room1'"
	cursor=conn.cursor()
	cursor.execute(str_query)
	conn.commit()
    

# add event listener on pin 21
GPIO.add_event_detect(40, GPIO.BOTH, callback=motionSensor, bouncetime=300)

GPIO.add_event_detect(37, GPIO.BOTH, callback=motionSensor, bouncetime=300)

try:
    while True:
        time.sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."
