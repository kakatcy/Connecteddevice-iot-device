'''
Created on Sep 27, 2019

@author: cytang
'''
from labs.module02.TempSensorEmulator import TempSensorEmulator
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.info("Module02 app start")
temp = TempSensorEmulator()
temp.run()
