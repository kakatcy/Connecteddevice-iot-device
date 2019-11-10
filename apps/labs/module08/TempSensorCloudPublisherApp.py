'''
Created on Nov 9, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
import random
from ubidots import ApiClient
from labs.module08.UbidotsClientConnector import UbidotsClientConnector

rootCertPath = "/Users/cytang/program/connected devices/ubidots_cert.pem"
topic = "/v1.6/devices/tcydevice/TempSensor"

class TempSensorCloudPublisherApp:
    json = None
    def client_pub(self):
        ubidotsClientConnector = UbidotsClientConnector()
        ubidotsClientConnector.connect()
        while True:
            temperature = random.uniform(0.0,50.0)
            print(temperature)
            ubidotsClientConnector.publish(topic, 0, temperature) 
            sleep(10) 

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    tempSensorCloudPublisherApp = TempSensorCloudPublisherApp()
    tempSensorCloudPublisherApp.client_pub() 