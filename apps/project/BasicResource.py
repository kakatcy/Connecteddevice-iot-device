from coapthon.resources.resource import Resource
from sense_hat import SenseHat
from project import SmtpClientConnector
import logging


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
        #when client call put, this method will be revoked
        self.payload = request.payload
        payloads = self.payload.split(',')
        air = float(payloads[0])
        water = float(payloads[1])
        
        if air != self.airconditioner:
            #display the temperature of air-conditioner on the LED screen of the SenseHat
            self.airconditioner = air
            senseHat = SenseHat()
            senseHat.show_message(payloads[0])
            
        if water != self.watering:
            self.watering = water
            #connect to smtp connector and send a email
            smtpClientConnector = SmtpClientConnector.SmtpClientConnector()
            smtpClientConnector.publishMessage("auto watering", "have automatically watered plants")
        logging.info("current actuator information"+self.payload)
        return self

    def render_POST(self, request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True