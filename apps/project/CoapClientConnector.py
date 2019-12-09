'''
Created on Nov 1, 2019

@author: cytang
'''
from coapthon.client.helperclient import HelperClient
import random
import logging
from time import sleep
from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil

class CoapClientConnector:
    client = None
    
    def __init__(self,serverAddr,port):
        #create a coap client
        self.client = HelperClient(server=(serverAddr, port))
    
    def runTests(self,resourceName):
        sense_hat = SenseHat()
        while True:
            #generated a random temperture data and created a sensordata object
            #temperature = random.uniform(0.0,30.0)  
            #humidity = random.uniform(30.0,40.0)
            
            #get sensor data from senseHat sensor
            temperature = sense_hat.get_temperature_from_humidity()
            humidity = sense_hat.get_humidity()
            sensorData = str(temperature) +','+ str(humidity) 
            logging.info(sensorData)
            #post the sensorData to the server
            response = self.client.post(resourceName, sensorData)
             
            sleep(60)  