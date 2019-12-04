'''
Created on Dec 1, 2019

@author: cytang
'''
from labs.module10.SensorDataPublisher import SensorDataPublisher

class SmartHomeAdaptor():
    
    def __init__(self):
        sensorDataPublisher = SensorDataPublisher()
        sensorDataPublisher.client_pub()