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
        if useTLS == True:
            client.username_pw_set("BBFF-B7HsNg1Sv3UESmoikX8oyyNxyx4jts","")
            client.tls_set(ca_certs=rootCertPath, certfile=None,
                           keyfile = None, cert_reqs = ssl.CERT_REQUIRED, 
                           tls_version = ssl.PROTOCOL_TLSv1_2, ciphers = None)
            client.tls_insecure_set(False)

    
    #connect to the broker
    def connect(self,client):
        logging.info("connecting")
        print("host:"+HOST)
     #   print("port:"+PORT)
        client.connect(HOST, PORT)
    
    def publish(self,client,topicName,qos,payload):
        client.publishMessage(topicName,payload)
        
    #subscribe topic from broker
    def subscribeToTopic(self,client,topicName):
        logging.info("subscribing")
        client.subscribe(topicName,2)
        sleep(10)
        client.unsubscribe(topicName)
    
    #disconnect from broker
    def disconnect(self,client):
        client.disconnect()
    

    