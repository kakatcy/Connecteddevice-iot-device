'''
Created on Dec 1, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from time import sleep
from project.MqttClientConnector import MqttClientConnector
from sense_hat import SenseHat
import random

rootCertPath = "/home/pi/workspace/iot-device/apps/labs/module10/ubidots_cert.pem"
topicMqttTemp = "temp"
topicMqttHumidity = "humidity"
topicTemp = "/v1.6/devices/finaldevice/temperature"
topicHumidity = "/v1.6/devices/finaldevice/humidity" 

#collect the temperature data
class SensorDataPublisher:
    client = None
    mqttClientConnector = None
    
    def client_pub(self):
        sense_hat = SenseHat()
        
        #MQTT
        client = mqtt.Client("pub_py") 
        mqttClientConnector = MqttClientConnector()
        
        #set the callback methods
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        #connect to the broker
        mqttClientConnector.connect(client)
        
        while True: 
            #get temperature 
            #temperature = sense_hat.get_temperature_from_humidity()
            temperature = random.uniform(0.0,45.0)
            logging.info("current temperature:" + str(temperature))
            mqttClientConnector.publishMessage(client,topicMqttTemp, 0, temperature) 
            logging.info("published temperature successfully")
            
            #get humidity 
            #humidity = sense_hat.get_humidity()
            humidity = random.uniform(45.0,60.0)
            logging.info("current humidity:" + str(humidity))
            mqttClientConnector.publishMessage(client, topicMqttHumidity, 0, humidity)
            logging.info("published humidity successfully")
            sleep(60)

    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected with result code "+str(rc))
    
    def on_disconnect(self, client, userdata, rc):
        logging.info("disconnecting reason "+ str(rc))      

    def on_message(self, client, userdata, msg):
        #log the jsondata that the subsriber received
        logging.info("the second json:\n" +str(msg.payload.decode("utf-8")))    
        logging.info("message topic="+str(msg.topic))
        logging.info("message qos="+str(msg.qos))
        logging.info("message retain flag="+str(msg.retain))    
        self.json = str(msg.payload.decode("utf-8"))
        #logging.info("the second json:\n" + self.json)