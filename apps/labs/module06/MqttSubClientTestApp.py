import paho.mqtt.client as mqtt
import logging
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil

HOST = "localhost"
PORT = 1883

class MqttSubClientTestApp:
    json = None
    def client_loop(self):
        client = mqtt.Client("sub_py")
        mqttClientConnector = MqttClientConnector()
        #set the callback methods
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        #connect to the broker
        mqttClientConnector.connect(client)
        client.loop_start()
        #subscribe topic from the broker
        mqttClientConnector.subscribeToTopic(client,"test")
        sleep(5)
        mqttClientConnector.disconnect(client)
        client.loop_stop()

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
    mqttSubClientTestApp = MqttSubClientTestApp()
    mqttSubClientTestApp.client_loop()    
    #if(mqttSubClientTestApp.json!=None):
    
    #convert the jsondata to sensedata object
    dataUtil = DataUtil()
    #print("json\n"+str(mqttSubClientTestApp.json))
    sensordata = dataUtil.toSensorDataFromJson(mqttSubClientTestApp.json)
    logging.info("sensordata converted from json:" + str(sensordata.getAvgValue()))
    
    #convert the sensedata object to jsondata again and log the third jsondata
    finaljson = dataUtil.toJsonFromSensorData(sensordata)
    logging.info("the third json:\n" + finaljson)