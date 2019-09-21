'''
Created on Sep 21, 2019

@author: cytang
'''

import logging
from time import sleep
from labs.module01 import SystemPerformanceAdaptor


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info("Starting system performance app daemon thread...")
    # If SystemPerformanceAdaptor extends from threading.Thread...
sysPerfAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
sysPerfAdaptor.daemon = True
sysPerfAdaptor.start()  
    
while (True):
    sleep(5)
    pass