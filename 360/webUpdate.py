import time
import RPi.GPIO as GPIO
import mysql.connector
GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering

conn=mysql.connector.connect(user='root', password='Nopassword01', host='172.16.34.81', database='autohome')

# Set relay pins as output
GPIO.setup(11, GPIO.OUT) #Light 1
GPIO.output(11, GPIO.LOW)

GPIO.setup(13, GPIO.OUT) #Light 2
GPIO.output(13, GPIO.LOW)

GPIO.setup(15, GPIO.OUT) #Fan
GPIO.output(15, GPIO.LOW)

cursor=conn.cursor()
try:
    while True:
        conn=mysql.connector.connect(user='root', password='Nopassword01', host='172.16.34.39', database='autohome')
        cursor=conn.cursor()
        query=("SELECT * from switch")
        cursor.execute(query)
        result=cursor.fetchone()
        #Check Light 1
        if (result[1] == 0):
            GPIO.output(11, GPIO.LOW)
        else:
            GPIO.output(11, GPIO.HIGH)
        #Check Light 2
        if (result[2] == 0):
            GPIO.output(13, GPIO.LOW)
        else:
            GPIO.output(13, GPIO.HIGH)
        #Check Fan
        if (result[3] == 0):
            GPIO.output(15, GPIO.LOW)
        else:
            GPIO.output(15, GPIO.HIGH)

        time.sleep(3)         # wait 1 second

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
