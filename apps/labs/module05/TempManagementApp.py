'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
from labs.module05.TempSensorAdaptorTask import TempSensorAdaptorTask

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.info("Module05 app start")
temp = TempSensorAdaptorTask()
#temp.daemon=True
temp.start()
