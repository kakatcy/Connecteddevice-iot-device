'''
Created on Sep 27, 2019

@author: cytang
'''
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.info("Module03 app start")
temp = TempSensorAdaptor()
#temp.daemon=True
temp.start()
#temp.run()
