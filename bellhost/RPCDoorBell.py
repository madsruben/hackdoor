#!/usr/bin/python
import serial
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#ser = serial.Serial('/dev/tty.usbserial', 9600)
#ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
dev = "/dev/ttyACM"

# sometimes the port falls out and the machine assigns a new port
global ser
# and that makes this little script a little ugly
def check_serial():
   try:
      ser.close()
   except:
      # nothing
      print "had no port, good thing we are reopening"

   for port in range(0, 9):
      print "doin it on "+ dev +str(port)
      try:
         ser = serial.Serial(dev+str(port), 9600)
         break
      except:
         print "port gone"
   if not ser:
      print "all ports are gone, silence"
   return ser

ser = check_serial()


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("0.0.0.0", 8000), requestHandler=RequestHandler)
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


