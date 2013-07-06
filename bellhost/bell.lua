#!/usr/bin/lua
-- lua

require "xmlrpc"
require "xmlrpc.http"

xmlrpc.http.call("http://localhost:8000/RPC2", "ring")
