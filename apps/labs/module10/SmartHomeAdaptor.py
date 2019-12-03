'''
Created on Dec 1, 2019

@author: cytang
'''
from labs.module10.AutoTemperature import AutoTemperature
from labs.module10.AutoWatering import AutoWatering
from time import sleep

class SmartHomeAdaptor():
    
    def __init__(self):
        autoTemperature = AutoTemperature()
        autoTemperature.client_pub()
        sleep(1)
        autoWatering = AutoWatering()
        autoWatering.client_pub()