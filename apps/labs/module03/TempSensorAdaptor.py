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


class TempSensorAdaptor(threading.Thread):
    threshold = 2
    
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        logging.info('Configuration data...\n' + str(self.config))
    
    def run(self):
        sensordata = SensorData.SensorData()
    #    senseHatLedActivator = SenseHatLedActivator.SenseHatLedActivator()
        senseledThread = SenseHatLedActivator.SenseHatLedActivator()
        senseledThread.start()
        #senseHatLedActivator.run()
        
        while True:
            sense = SenseHat()
            temperature = sense.get_temperature()
            sensordata.addValue(temperature)
            
            #smtp module
            if(abs(sensordata.getValue()-sensordata.getAvgValue())>=self.threshold):
                logging.info('\n  Current temp exceeds average by > ' + str(self.threshold) + '. Triggering alert...')
                smtpClientConnector = SmtpClientConnector.SmtpClientConnector()
                smtpClientConnector.publishMessage("Excessive Temp", sensordata)
                
            nomialtemp = self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.NOMINAL_TEMP_KEY)
            
            #senseHat Led module
            if(sensordata.getValue != nomialtemp):
                logging.info('\n temperature is different from nomialtemp')
                actuatordata = ActuatorData()   
                actuatordata.command = 1
                actuatordata.statusCode = 1
                actuatordata.errCode = 0
                actuatordata.val = temperature
                actuatordata.stateData = temperature - float(nomialtemp)
                TempActuatorEmulator().processMessage(actuatordata, senseledThread)
            time.sleep(10)