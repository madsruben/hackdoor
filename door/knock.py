#!/usr/bin/python

import xmlrpclib

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def knock():
    if request.method == 'POST':
        try:
            s = xmlrpclib.ServerProxy('http://localhost:8000')
            if request.form['person']:
                person = request.form['person']
            else:
                person = '<anonymous>'
            ircText = '!! %s knocked at the door from %s. Please open.' % (person, request.remote_addr)
            retCode = s.say('#oslohackerspace', ircText)
       	    t = xmlrpclib.ServerProxy('http://localhost:8101')
            ret2 = t.ring()
        except:
            retcode = "epic fail!!! :D"
        else:
            retcode = "epic success! :-]"
        return render_template('knocked.html', knockresponse=retcode)
    else:
        return render_template('index.html')

@app.route("/mu-dd4bffbb-ff2e9926-5a80952c-1cb0374f")
def blitz():
	return "42"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


