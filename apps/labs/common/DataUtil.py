'''
Created on Oct 13, 2019

@author: cytang
'''
from labs.common import ActuatorData
import json
from labs.common import SensorData

class DataUtil():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def toJsonFromSensorData(self, sensordata):
        pass
    
    def toSensorDataFromJson(self, jsonData):
        sdDict = json.loads(jsonData)
        #print(" decode [pre]  --> " + str(sdDict))
        sd= SensorData.SensorData()
        sd.name= sdDict['name']
        sd.timeStamp= sdDict['timeStamp']
        sd.avgValue= sdDict['avgValue']
        sd.minValue= sdDict['minValue']
        sd.maxValue= sdDict['maxValue']
        sd.curValue= sdDict['curValue']
        sd.totValue= sdDict['totValue']
        sd.sampleCount = sdDict['sampleCount']
        #print(" decode [post] --> " + str(sd))
        return sd
    
    def toSensorDataFromJsonFile(self,filename,path):
        pass
    
    def toJsonFromActuatorData(self,actuatordata):
        pass
    
    def toActuatorDataFromJson(self,jsonData):
        adDict = json.loads(jsonData)
        #print(" decode [pre]  --> " + str(adDict))
        ad= ActuatorData.ActuatorData()
        ad.name= adDict['name']
        ad.timeStamp= adDict['timeStamp']
        ad.hasError= adDict['hasError']
        ad.command= adDict['command']
        ad.errCode= adDict['errCode']
        ad.statusCode  = adDict['statusCode']
        ad.stateData   = adDict['stateData']
        ad.curValue    = adDict['curValue']
        #print(" decode [post] --> " + str(ad))
        return ad
    
    def toActuatorDataFromJsonFile(self,filename,path):
        pass