'''
Created on Dec 8, 2019

@author: cytang
'''
from coapthon.resources.resource import Resource
from sense_hat import SenseHat
from project import SmtpClientConnector


class BasicResource(Resource):
    airconditioner = 0.0
    watering = 0.0
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Basic Resource"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        payloads = self.payload.split(',')
        air = float(payloads[0])
        water = float(payloads[1])
        
        if air != self.airconditioner:
            self.airconditioner = air
            senseHat = SenseHat()
            senseHat.show_message(payloads[0])
            
        if water != self.watering:
            self.watering = water
            smtpClientConnector = SmtpClientConnector.SmtpClientConnector()
            smtpClientConnector.publishMessage("auto watering", "have automatically watered plants")
        
        print(self.payload)
        return self

    def render_POST(self, request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True