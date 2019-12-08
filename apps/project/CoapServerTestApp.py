from coapthon.server.coap import CoAP
from project import BasicResource

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('temp1/', BasicResource())

def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        #print "Server Shutdown"
        print("Server Shutdown")
        server.close()
        print("Exiting...")
        #print "Exiting..."
        
if __name__ == '__main__':
    main()