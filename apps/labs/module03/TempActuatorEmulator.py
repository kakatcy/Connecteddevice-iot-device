'''
Created on Oct 3, 2019

@author: cytang
'''
import threading
from labs.common.ActuatorData import ActuatorData
from labs.module03.SimpleLedActivator import SimpleLedActivator
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

class TempActuatorEmulator(ActuatorData):
    actuatordata = ActuatorData()
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
    def processMessage(self, actuatordata, senseHatLedActivator):
        gap = actuatordata.val - self.actuatordata.val
        if(gap!=0):
            self.actuatordata.updateData(actuatordata)
            #senseHatLedActivator = SenseHatLedActivator()
            senseHatLedActivator.setEnableLedFlag(True)
            print(self.actuatordata.getStateData())
            #senseHatLedActivator.setDisplayMessage(self.actuatordata.getStateData())
            senseHatLedActivator.setDisplayMessage(round(self.actuatordata.getStateData(), 3))