'''
Created on Dec 8, 2019

@author: cytang
'''
from coapthon.resources.resource import Resource

class SourceHandler(Resource):
    def __init__(self, name="ResourceHandler", coap_server=None):
        super(SourceHandler, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
    def handle_POST(self, request):
        payload = request.payload
        print(payload)
        return payload