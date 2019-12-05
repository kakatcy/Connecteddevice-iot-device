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
PORT = 8883

class MqttClientConnector:
    def __init__(self,client, useTLS, rootCertPath):
        #using ssl to connect ubidots
        if useTLS == True:
            #set username and password
            client.username_pw_set("BBFF-B7HsNg1Sv3UESmoikX8oyyNxyx4jts","")
            client.tls_set(ca_certs=rootCertPath, certfile=None,
                           keyfile = None, cert_reqs = ssl.CERT_REQUIRED, 
                           tls_version = ssl.PROTOCOL_TLSv1_2, ciphers = None)
            client.tls_insecure_set(False)

    
    #connect to the broker
    def connect(self,client):
        logging.info("connecting")
        client.connect(HOST, PORT)
        logging.info("connected successfully")
    
    def publish(self,client,topicName,qos,payload):
        client.publishMessage(topicName,payload)
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
    

    