'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
import threading
import time
#import random
from labs.common import SensorData
from labs.module02 import SmtpClientConnector
from labs.module03 import SenseHatLedActivator
from sense_hat import SenseHat

from labbenchstudios.common import ConfigConst
from labbenchstudios.common import ConfigUtil
from labs.common.ActuatorData import ActuatorData
from labs.module03.TempActuatorEmulator import TempActuatorEmulator
from labs.common.DataUtil import DataUtil


class TempSensorAdaptorTask(threading.Thread):
    threshold = 2
    
    def __init__(self):
        super(TempSensorAdaptorTask,self).__init__()
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        logging.info('Configuration data...\n' + str(self.config))
    
    def run(self):
        sensordata = SensorData.SensorData()
        
        while True:
            sense = SenseHat()
            #generate new temperature data
            temperature = sense.get_temperature() 
            sensordata.addValue(temperature)
            #add into log
            logging.info("\n---------------------------------\nNew sensor readings:\n"+
                         "name="+sensordata.name + ",timeStamp=" +sensordata.timeStamp+
                         ",minValue=" + str(sensordata.minValue)+ ",aveValue="+ str(sensordata.avgValue)+
                         ",maxValue=" + str(sensordata.maxValue)+ ",curValue=" + str(sensordata.curValue)+
                         ",totValue=" + str(sensordata.totValue)+ ",sampleCount=" +str(sensordata.sampleCount))
            
            #convert to json format from python object
            datautil = DataUtil()
            jsondata = datautil.toJsonFromSensorData(sensordata)
            if(abs(sensordata.curValue - sensordata.avgValue)>2):
                logging.info("\nCurrent temp exceeds average by >2. Converting data...\n"+
                             "JSON data:\n" + jsondata)
            
            #smtp module
            smtpClientConnector = SmtpClientConnector.SmtpClientConnector()
            smtpClientConnector.publishMessage("Temperature", jsondata)
            # logging.info("send email successfully")
            
            #write json dta to filesystem
            of = open("tempData.json", "w+")
            of.write(jsondata)
            of.close()
            # logging.info("write data as JSON file to filesystem successfully")
            
            time.sleep(10)