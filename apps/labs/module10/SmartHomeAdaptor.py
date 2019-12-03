'''
Created on Dec 1, 2019

@author: cytang
'''
from labs.module10.AutoTemperature import AutoTemperature
from labs.module10.AutoWatering import AutoWatering

class SmartHomeAdaptor():
    
    def __init__(self):
        autoTemperature = AutoTemperature()
        autoTemperature.client_pub()
        
        autoWatering = AutoWatering()
        autoWatering.client_pub()