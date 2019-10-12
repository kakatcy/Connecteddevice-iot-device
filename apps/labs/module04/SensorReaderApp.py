'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
from labs.module04.I2CSenseHatAdaptor import I2CSenseHatAdaptor
from labs.module04.SenseHatDeviceAdaptor import SenseHatDeviceAdaptor

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.info("Module04 app start")
humidity_i2c = I2CSenseHatAdaptor()
humidity_i2c.start()
humidity_sensehat = SenseHatDeviceAdaptor()
humidity_sensehat.start()
