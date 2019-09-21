'''
Created on Sep 21, 2019

@author: cytang
'''
import threading
import logging
import time
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceAdaptor (threading.Thread):
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    
    def run(self):
        count = 10
        while count>0:
                sysCpuUtilTask = SystemCpuUtilTask()
                cpuUtil  = sysCpuUtilTask.getDataFromSensor()
                sysMemUtilTask = SystemMemUtilTask()
                memUtil  = sysMemUtilTask.getDataFromSensor()
                perfData = 'CPU Utilization=' + str(cpuUtil)
                logging.info(perfData)
                perfData =  "Memory Utilization=" + str(memUtil)
                logging.info(perfData)
                time.sleep(5)
                count=count-1