'''
Created on Dec 8, 2019

@author: cytang
'''
from coapthon.resources.resource import Resource

class SourceHandler(Resource):
    def handle_POST(self, request):
        payload = request.payload
        print(payload)
        return payload