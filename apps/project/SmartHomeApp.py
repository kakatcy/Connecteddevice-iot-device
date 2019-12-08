'''
Created on Dec 1, 2019

@author: cytang
'''
from project.SmartHomeAdaptor import SmartHomeAdaptor
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info("Starting smart home system performance app daemon thread...")

smartHomeAdaptor = SmartHomeAdaptor()