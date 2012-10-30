#!/usr/bin/python
import serial
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#ser = serial.Serial('/dev/tty.usbserial', 9600)
#ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("0.0.0.0", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

def ringBell():
    ser.write('R')
    return 'ok'

def alarmBell():
    ser.write('Z')
    return 'ok'

server.register_function(ringBell, 'ring')
server.register_function(alarmBell, 'alarm')

server.serve_forever()

