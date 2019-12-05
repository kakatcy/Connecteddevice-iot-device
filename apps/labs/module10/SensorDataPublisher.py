'''
Created on Dec 1, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module10.UbidotsConnector import UbidotsConnector
from sense_hat import SenseHat

rootCertPath = "/home/pi/workspace/iot-device/apps/labs/module10/ubidots_cert.pem"
topicTemp = "/v1.6/devices/finaldevice/temperature"
topicHumidity = "/v1.6/devices/finaldevice/Humidity" 

#collect the temperature data
class SensorDataPublisher:
    json = None
    def client_pub(self):
        sense_hat = SenseHat()
        #ubidots
        ubidotsConnector = UbidotsConnector()
        ubidotsConnector.connect()
        
        #MQTT
        client = mqtt.Client("pub_py") 
        mqttClientConnector = MqttClientConnector(client,True,rootCertPath)
        #set the callback methods
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        #connect to the broker
        mqttClientConnector.connect(client)
        while True:
            #get temperature 
            temperature = sense_hat.get_temperature_from_humidity()
            logging.info("current temperature:" + str(temperature))
            
            #publish the temperature to ubidots by using ubidots API
            #ubidotsConnector.publishTemp(topicTemp, 0, temperature)
            
            #publish the current temperature to ubidots by mqtt
            client.publish(topicTemp, temperature, 1, True) 
            logging.info("published temperature successfully")
            
            #get humidity 
            humidity = sense_hat.get_humidity()
            logging.info("current humidity:" + str(humidity))
            ubidotsConnector.publishHumidity(topicHumidity, 0, humidity)
            logging.info("published humidity successfully")
            sleep(60) 

    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected with result code "+str(rc))
        client.subscribe("test",qos=2)
    
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