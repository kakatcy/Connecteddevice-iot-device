'''
Created on Dec 1, 2019

@author: cytang
'''
from project.SensorDataPublisher import SensorDataPublisher

class SmartHomeAdaptor():
    
    def __init__(self):
        sensorDataPublisher = SensorDataPublisher()
        sensorDataPublisher.client_pub()