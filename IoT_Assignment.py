#!/usr/bin/python3

from urllib.request import urlopen
import  json
import  time
from sense_hat import SenseHat

WRITE_API_KEY='6D7NQK57KT5UPZ0Y'

baseURL='https://api.thingspeak.com/update?api_key=6D7NQK57KT5UPZ0Y' 

sense = SenseHat()

def writeData(temp, humid):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (temp) + '&field2=%s' % (humid))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    temp=round(sense.get_temperature(),2)
    humid=round(sense.get_humidity(),2)    
    writeData(temp, humid)
    time.sleep(20)
