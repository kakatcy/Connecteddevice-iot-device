'''
Created on Oct 24, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from time import sleep
from paho.mqtt.subscribe import _on_message_callback

HOST = "localhost"
PORT = 1883

class MqttClientConnector:
    #connect to the broker
    def connect(self,client):
        logging.info("connecting")
        client.connect(HOST, PORT, 70)
    
    #subscribe topic from broker
    def subscribeToTopic(self,client,topicName):
        logging.info("subscribing")
        client.subscribe(topicName,2)
        sleep(10)
        client.unsubscribe(topicName)
    
    #disconnect from broker
    def disconnect(self,client):
        client.disconnect()
    

    