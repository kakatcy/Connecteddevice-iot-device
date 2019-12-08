'''
Created on Dec 8, 2019

@author: cytang
'''
from coapthon.server.coap import CoAP
from project.SourceHandler import SourceHandler

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('temp1/',SourceHandler())
        
def main():
    server = CoAPServer("0.0.0.0", 5683)
    print("server is running")
    #try:
        #server.listen(10)
        
if __name__ == '__main__':
    main()