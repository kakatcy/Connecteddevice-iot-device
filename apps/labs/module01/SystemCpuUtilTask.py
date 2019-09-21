'''
Created on Sep 21, 2019

@author: cytang
'''
import psutil;

class SystemCpuUtilTask():
    def getDataFromSensor(self):
        cpurate = psutil.cpu_percent(5)
        return cpurate