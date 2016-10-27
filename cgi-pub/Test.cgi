#! /usr/bin/env python
import flask
import time

#print "Content-type: text/html"
#print
#
#print """
#<html>
#
#<head>
#<title>ProbAnno</title>
#</head>
#
#<body>
#
  #<h3> ProbAnno </h3>
#"""

app = flask.Flask(__name__)

@app.route('/yield')
def index():
    def inner():
        for x in range(100):
            time.sleep(1)
            yield '%s<br/>\n' % x
    return flask.Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately

app.run(debug=True)

#print """
#
#
#</body>
#
#</html>
#""" 
