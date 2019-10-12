'''
Created on Oct 7, 2019

@author: cytang
'''
import threading
import logging
from time import sleep
from sense_hat import SenseHat

class SenseHatDeviceAdaptor(threading.Thread):
    sense_hat = SenseHat()

    def __init__(self):
        super(SenseHatDeviceAdaptor,self).__init__()
        pass
    
    #get humidity by using sensehat python package
    def displayHumidity(self):
        humidity = self.sense_hat.get_humidity()
        return humidity
        #logging.info("humidity from sensehat:" + str(humidity))
    
    #get temperature by using sensehat python package
    def displayTemp(self):
        temp = self.sense_hat.get_temperature_from_humidity()
        return temp
        #logging.info("temperature from sensehat:" + str(temp))
        
    def run(self):
        while True:
            humidity = round(self.displayHumidity(),2)
            temp = round(self.displayTemp(),2)
            logging.info("humidity_sensehat:" + str(humidity) + " temp_sensehat:"+str(temp))
            sleep(5)