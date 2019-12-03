'''
Created on Dec 1, 2019

@author: cytang
'''
from ubidots.apiclient import ApiClient

class UbidotsConnector:
    api=None
    
    def connect(self):
        #connect to the ubidots
        self.api = ApiClient(token = "BBFF-B7HsNg1Sv3UESmoikX8oyyNxyx4jts")
    
    
    def publishTemp(self,topicName,qos,payload): 
        #get the variable by ID, and publish payload to ubidots
        var = self.api.get_variable("5de42e6e1d84725dc4107c0f")     #temperature
        var.save_value({'value':payload})
        
    def publishHumidity(self,topicName,qos,payload):
        #get the variable by ID, and publish payload to ubidots
        var = self.api.get_variable("5de42e7e1d84725d134ed82e")     #humidity
        var.save_value({'value':payload})
        