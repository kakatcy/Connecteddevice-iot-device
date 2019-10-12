'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
from labs.module04.I2CSenseHatAdaptor import I2CSenseHatAdaptor
from labs.module04.SenseHatDeviceAdaptor import SenseHatDeviceAdaptor

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.info("Module04 app start\n")
adaptor_i2c = I2CSenseHatAdaptor()
adaptor_i2c.start()
deviceadaptor_sensehat = SenseHatDeviceAdaptor()
deviceadaptor_sensehat.start()
