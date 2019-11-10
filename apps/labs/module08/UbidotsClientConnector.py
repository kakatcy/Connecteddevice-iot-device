'''
Created on Nov 9, 2019

@author: cytang
'''
from ubidots.apiclient import ApiClient

class UbidotsClientConnector:
    api=None
    
    def connect(self):
        self.api = ApiClient(token = "BBFF-B7HsNg1Sv3UESmoikX8oyyNxyx4jts")
    
    
    def publish(self,topicName,qos,payload): 
        var = self.api.get_variable("5dc7337d1d847235ca5b5e3e")
        var.save_value({'value':payload})