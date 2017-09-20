hackdoor
========

hackeriet doorbell


bellhost/         : connect the XMLRPC service with the 
   run            : runscript to start everything
   RPCDoorBell    : daemon translates XMLRPC to serial requests
   doorconn.sh    : connect & port forward to webhost
   ring.lua       : rings on XMLRPC
   alarm.lua      : alarms on XMLRPC



arduino/ : arduino code that takes 9600baud serial characters
and controls the bell on pin 8.

"R" - Ring once, "Z" - Ring alarm 

Connection diagram
of relay circuit

A - GND (brown)
B - PIN (yellow)
C - VCC (red)
x - NONE
x - NONE
O - BELL± (blue)
O - BELL± (blue)




