'''
Created on Nov 1, 2019

@author: cytang
'''
from coapthon.client.helperclient import HelperClient
import random
import logging
from time import sleep
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil

class CoapClientConnector:
    client = None
    
    def __init__(self,serverAddr,port):
        #create a coap client
        self.client = HelperClient(server=(serverAddr, port))
    
    def runTests(self,resourceName):
        while True:
            #generated a random temperture data and created a sensordata object
            temperature = random.uniform(0.0,30.0)  
            humidity = random.uniform(30.0,40.0)
            #sensordata.addValue(temperature)
            sensorData = str(temperature) +','+ str(humidity) 
            '''
            #created DataUtil instance and converted the sensordata to json data
            datautil = DataUtil()
            jsondata = datautil.toJsonFromSensorData(sensordata) 
            print("the first json:\n" + jsondata)
            '''
        
            #post the jsondata to the server
            
            response = self.client.post(resourceName, sensorData)
             
            #logging.info(response.pretty_print())

            '''
            #get data from the server
            response = self.client.get(resourceName)
            logging.info(response.pretty_print())

            #put jsondata to the server
            response = self.client.put(resourceName, str(temperature), None, 10)
            logging.info(response.pretty_print())

            #delete resources
            response = self.client.delete(resourceName, None, 10)
            logging.info(response.pretty_print())
            '''
            sleep(10)

            #stop the client
            #self.client.stop()    