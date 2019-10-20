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


    def __init__(self):
        '''
        Constructor
        '''
    
    #convert sensordata to json format    
    def toJsonFromSensorData(self,sensordata):

        jsondata = {"name":sensordata.name , "timeStamp":sensordata.timeStamp,
                "minValue":sensordata.minValue , "avgValue":sensordata.avgValue,
                "maxValue":sensordata.maxValue, "curValue":sensordata.curValue,
                "totValue":sensordata.totValue, "sampleCount":sensordata.sampleCount}
        result = json.dumps(jsondata)
    #    print(result)
        return result
    
    #convert jsondata to sensordata object    
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
    
    #read json file from a file path and then convert it to sensor data object    
    def toSensorDataFromJsonFile(self,filename,path):
        of = open(filename + path,"r+")
        jsondata = of.read()
    #    print(jsondata)
        sd = self.toSensorDataFromJson(jsondata)
        of.close()
        return sd
        pass
    
    #convert actuatordata to json format    
    def toJsonFromActuatorData(self,actuatordata):
        json = {"name":actuatordata.name , "timeStamp":actuatordata.timeStamp,
                "hasError":actuatordata.hasError , "command":actuatordata.command,
                "errCode":actuatordata.errCode , "statusCode":actuatordata.statusCode,
                "stateData":actuatordata.stateData , "curValue":actuatordata.curValue}
        result = json.dump(json)
    #    print(result)
        return result
        pass
    
    #convert jsondata to actuator object    
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
    
    #read json file from a file path and then convert it to actuator data object
    def toActuatorDataFromJsonFile(self,filename,path):
        of = open(filename + path,"r+")
        jsondata = of.read()
    #   print(jsondata)
        sd = self.toActuatorDataFromJson(jsondata)
        of.close()
        return sd
        pass