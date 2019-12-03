'''
Created on Dec 1, 2019

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
from labs.module10.UbidotsConnector import UbidotsConnector
from sense_hat import SenseHat

rootCertPath = "/Users/cytang/program/connected devices/ubidots_cert.pem"
topicTemp = "/v1.6/devices/finaldevice/Temperature"
topicHumidity = "/v1.6/devices/finaldevice/Humidity"

#collect the temperature data
class AutoTemperature:
    json = None
    def client_pub(self):
        sense_hat = SenseHat()
        ubidotsConnector = UbidotsConnector()
        ubidotsConnector.connect()
        while True:
            #get temperature 
            temperature = sense_hat.get_temperature_from_humidity()
            logging.info("current temperature:" + str(temperature))
            #publish the temperature to ubidots by using ubidots API
            ubidotsConnector.publishTemp(topicTemp, 0, temperature)
            
            logging.info("published successfully")
            sleep(60) 