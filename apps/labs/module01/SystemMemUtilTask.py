'''
Created on Sep 21, 2019

@author: cytang
'''
import psutil;

class SystemMemUtilTask():        
    def getDataFromSensor(self):
        memrate = psutil.virtual_memory().percent
        return memrate