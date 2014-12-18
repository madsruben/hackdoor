#!/usr/bin/python
import serial
import socket
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# sometimes the port falls out and the machine assigns a new port
global ser
#ser = serial.Serial('/dev/tty.usbserial', 9600)
#ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
#ser = serial.Serial('/dev/ttyACM1', 9600)
dev = "/dev/ttyBELL"

low = 1
hi  = 9

# and that makes this little script a little ugly
def check_serial():
   try:
      ser.close()
   except:
      # nothing
      print "had no port, good thing we are reopening"

   print "doin it on " + dev
   try:
      ser = serial.Serial(dev, 9600)
   except Exception as e:
      print "port gone: " + str(e)
   if not ser:
      print "all ports gone, try again"
   return ser
    

   for port in range(low, hi):
      print "doin it on "+ dev +str(port)
      try:
         ser = serial.Serial(dev+str(port), 9600)
         break
      except Exception as e:
         print "port gone: " + str(e)
   if not ser:
      print "all ports are gone, silence"
   return ser

ser = check_serial()


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

SimpleXMLRPCServer.address_family = socket.AF_INET6
server = SimpleXMLRPCServer(("", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

def ringBell():
    print "breaK WIND"
    ser = check_serial()
    ser.write('R')
    return 'ok'

def alarmBell():
    print "hALARM"
    ser = check_serial()
    ser.write('Z')
    return 'ok'

server.register_function(ringBell, 'ring')
server.register_function(alarmBell, 'alarm')

server.serve_forever()


