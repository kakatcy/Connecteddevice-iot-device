'''
Created on Oct 24, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from time import sleep
from paho.mqtt.subscribe import _on_message_callback
import ssl

HOST = "industrial.api.ubidots.com"
PORT = 1883

class MqttClientConnector:
    #connect to the broker
    def connect(self,client):
        logging.info("connecting")
        client.connect(HOST, PORT)
        logging.info("connected successfully")
    
    def publishMessage(self,client,topicName,qos,payload):
        client.publish(topicName,payload)
        logging.info("data have published")
        
    #subscribe topic from broker
    def subscribeToTopic(self,client,topicName):
        logging.info("subscribing")
        client.subscribe(topicName,0)
        sleep(10)
        client.unsubscribe(topicName)
    
    #disconnect from broker
    def disconnect(self,client):
        client.disconnect()
    

    