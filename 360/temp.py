import time
import mysql.connector

conn=mysql.connector.connect(user='root', password='Nopassword01', host='172.16.34.39', database='autohome')
try:
        while True:
                tempfile = open("/sys/bus/w1/devices/28-0000073ebc1c/w1_slave")
                thetext = tempfile.read()
                tempfile.close()
                tempdata = thetext.split("\n")[1].split(" ")[9]
                temperature = float(tempdata[2:])
                temperature = temperature / 1000
                print temperature

	
		
		str_query = "INSERT INTO temp values('"+str(temperature)+"')"
		cursor=conn.cursor()
		cursor.execute(str_query)
		conn.commit()
	
                time.sleep(5)
except KeyboardInterrupt:
        pass




