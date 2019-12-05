'''
Created on Dec 1, 2019

@author: cytang
'''
import paho.mqtt.client as mqtt
import logging
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

rootCertPath = "/home/pi/workspace/iot-device/apps/labs/module10/ubidots_cert.pem"
#topicAirconditioner = "/v1.6/devices/finaldevice/AirconditionerSetting"
topicAirconditioner = "/v1.6/devices/finaldevice/temperature/lv"
topicWatering = "/v1.6/devices/finalDevice/Watering"

class ActuatorDataSubscriber:
    def client_sub(self):
        client = mqtt.Client("sub_py")
        mqttClientConnector = MqttClientConnector(client,True,rootCertPath)
       
        #connect to the broker
        mqttClientConnector.connect(client)

        #subscribe topic from the broker
        #mqttClientConnector.subscribeToTopic(client,topicAirconditioner)
        #client.subscribe(topicAirconditioner, 1)
        
        #set the callback methods
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected with result code "+str(rc))
        client.subscribe(topicAirconditioner,qos=1)
    
    def on_disconnect(self, client, userdata, rc):
        logging.info("disconnecting reason "+ str(rc))

    def on_message(self, client, userdata, msg):
        logging.info("the second json:\n" +str(msg.payload.decode("utf-8")))    
        logging.info("message topic="+str(msg.topic))
        logging.info("message qos="+str(msg.qos))
        logging.info("message retain flag="+str(msg.retain))    
        #self.json = str(msg.payload.decode("utf-8"))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    actuatorDataSubscriber = ActuatorDataSubscriber()
    actuatorDataSubscriber.client_sub()    
