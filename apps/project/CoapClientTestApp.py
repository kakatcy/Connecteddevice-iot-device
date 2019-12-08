'''
Created on Nov 1, 2019

@author: cytang
'''

import logging
from project.CoapClientConnector import CoapClientConnector

class CoapClientTest:
    def coapclient(self):
        host = '10.0.0.60'
        port = 5683
        #invoke coapclientconnector to connect the server
        coapClientConnector = CoapClientConnector(host, port)
        coapClientConnector.runTests("temp")
        
    
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    coapClientTest = CoapClientTest()
    coapClientTest.coapclient()  
