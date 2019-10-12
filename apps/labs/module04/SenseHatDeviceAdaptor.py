'''
Created on Oct 7, 2019

@author: cytang
'''
import threading
from time import sleep
from sense_hat import SenseHat

class SenseHatDeviceAdaptor(threading.Thread):


    def __init__(self):
        super(SenseHatDeviceAdaptor,self).__init__()
        pass
    
    def displayHumidity(self):
        sense_hat = SenseHat()
        humidity = sense_hat.get_humidity()
        print("sensehat humidity:" + str(humidity))
    
    def displayTemp(self):
        sense_hat = SenseHat()
        temp = sense_hat.get_temperature_from_humidity()
        print("sensehat temp:" + str(temp))
        
    def run(self):
        while True:
            #self.displayHumidity()
            self.displayTemp()
            sleep(5)