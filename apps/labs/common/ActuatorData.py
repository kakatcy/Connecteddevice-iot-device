'''
Created on Oct 3, 2019

@author: cytang
'''

import os
from datetime import datetime

COMMAND_OFF =0
COMMAND_ON  =1
COMMAND_SET =2
COMMAND_RESET = 3

STATUS_IDLE   = 0
STATUS_ACTIVE = 1

ERROR_OK =0 
ERROR_COMMAND_FAILED = 1 
ERROR_NON_RESPONSIBLE = -1

class ActuatorData():
    timeStamp = None
    name = 'Not set'
    hasError = False
    command = 0
    errCode = 0
    statusCode = 0
    stateData = None
    val = 0.0

    def __init__(self):
        self.updateTimeStamp()
        
    def getCommand(self):
        return self.command
    def getStatusCode(self):
        return self.statusCode
    def getErrorCode(self):
        return self.errCode
    def getStateData(self):
        return self.stateData
    def getValue(self):
        return self.val
    
    def updateData(self, data):
        self.command    = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode    = data.getErrorCode()
        self.stateData  = data.getStateData()
        self.val        = data.getValue()
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
        

        