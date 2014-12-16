#!/usr/bin/python

import xmlrpclib

from redis import Redis
from flask import Flask, render_template, request
def irc_say(msg):
    fd = open("/irc/server/in", "w")
    fd.write("/j #oslohackerspace")
    fd.close()
    fd = open("/irc/server/#oslohackerspace/in", "w")
    print("got %s, %s" % (fd, msg))
    fd.write(msg + "\n")
    fd.close()
    return "Wtf"

def xmlrpc_irc_say(self, msg):
    try:
        s = xmlrpclib.ServerProxy('http://localhost:8181')
        retcode = s.say('#oslohackerspace', msg)
    except:
        retcode = "no irc message"

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def knock():
    db = Redis()
    #if db.get('lastknock'):
    #    return render_template('toosoon.html')

    if request.method == 'POST':
        if request.form['person']:
            person = request.form['person']
        else:
            person = '<anonymous>'
        
        try:
            db.setex('lastknock', person, 120) # 120 seconds timeout
        except:
            retcode = "no lastknock"

        addr = request.remote_addr
        if addr == "::1" or addr == "localhost" or addr == "127.0.0.1" and request.headers['x-forwarded-for']:
            addr = request.headers['x-forwarded-for']

        try:
            t = xmlrpclib.ServerProxy('http://localhost:8000')
            ret2 = t.ring()
        except:
            retcode = "epic fail!!! :D"
        else:
            retcode = "epic success! :-]"

        # write to IRC
        ircText = '!! %s knocked at the door from %s. Please open.' % (person, addr)
        print("%s, status: %s" % (ircText, retcode))
        irc_say(ircText)

        return render_template('knocked.html', knockresponse=retcode)

    else:
        return render_template('index.html')

@app.route("/mu-dd4bffbb-ff2e9926-5a80952c-1cb0374f")
def blitz():
    return "42"

if __name__ == "__main__":
    app.run(host='::', debug=True)


