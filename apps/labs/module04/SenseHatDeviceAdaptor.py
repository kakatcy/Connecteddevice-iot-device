'''
Created on Oct 7, 2019

@author: cytang
'''
import threading
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
        print("humidity from sensehat:" + str(humidity))
    
    #get temperature by using sensehat python package
    def displayTemp(self):
        temp = self.sense_hat.get_temperature_from_humidity()
        print("temperature from sensehat:" + str(temp))
        
    def run(self):
        while True:
            self.displayHumidity()
            self.displayTemp()
            sleep(5)