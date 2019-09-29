'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
import threading
import time
import random
from labs.common import SensorData
from labs.module02 import SmtpClientConnector


class TempSensorEmulator(threading.Thread):
    threshold = 5
    
    def run(self):
        count =10
        sensordata = SensorData.SensorData()
        while count>0:
            #generate a random temperature in [0,30]
            temperature = random.uniform(0.0,30.0)  
            sensordata.addValue(temperature)
        #    self.sendNotification()
        #check if the temperature is surpass the threshold
            if(abs(sensordata.getValue()-sensordata.getAvgValue())>=self.threshold):
                logging.info('\n  Current temp exceeds average by > ' + str(self.threshold) + '. Triggering alert...')
                smtpClientConnector = SmtpClientConnector.SmtpClientConnector()
                smtpClientConnector.publishMessage("Excessive Temp", sensordata)
            count=count-1
            time.sleep(30)