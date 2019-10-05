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
        
        
    def processMessage(self, data, senseHatLedActivator):
        gap = data.val - self.actuatordata.val
        if(gap!=0):
            self.actuatordata.updateData(data)
            print("renewed temperature")
            print(self.actuatordata.val)
            if(gap>0):
                print("increase ")
                print(gap)
            if(gap<0):
                print("decrease ")
                print(gap)
            #senseHatLedActivator = SenseHatLedActivator()
            senseHatLedActivator.setEnableLedFlag(True)
            senseHatLedActivator.setDisplayMessage(self.actuatordata.val)
        #    self.senseHatLedActivator.run() 
            #print("1111111") 
         #   thread.start(SenseHatLedActivator.run(),"display",2)
         #   t1 = threading.Thread(target=SenseHatLedActivator,args=())
         #   t1.start()
        
            #senseHatLedActivator.run()
            #print("0000000")