'''
Created on Nov 9, 2019

@author: cytang
'''
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

HOST = "localhost"
PORT = 1883
rootCertPath = "/Users/cytang/program/connected devices/ubidots_cert.pem"
topic = "/v1.6/devices/tcydevice/TempSensor"

class TempSensorPublisherApp:
    json = None
    def client_pub(self):
        client = mqtt.Client("pub_py")
        mqttClientConnector = MqttClientConnector(client,True,rootCertPath)
        #set the callback methods
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        #connect to the broker
        mqttClientConnector.connect(client)
        while True:
            temperature = random.uniform(0.0,50.0)
            print(temperature)
            client.publish(topic, temperature, 1, True) 
            sleep(10) 
        #client.loop_start()
        
        #subscribe topic from the broker
        #   mqttClientConnector.subscribeToTopic(client,"test")
     
        #   sleep(5)
        #mqttClientConnector.disconnect(client)
        #client.loop_stop()

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

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    tempSensorPublisherApp = TempSensorPublisherApp()
    tempSensorPublisherApp.client_pub()    
    #if(mqttSubClientTestApp.json!=None):
    
    '''
    #convert the jsondata to sensedata object
    dataUtil = DataUtil()
    #print("json\n"+str(mqttSubClientTestApp.json))
    sensordata = dataUtil.toSensorDataFromJson(tempActuatorSubscriberApp.json)
    logging.info("sensordata converted from json:" + str(sensordata.getAvgValue()))
    
    #convert the sensedata object to jsondata again and log the third jsondata
    finaljson = dataUtil.toJsonFromSensorData(sensordata)
    logging.info("the third json:\n" + finaljson)
    '''