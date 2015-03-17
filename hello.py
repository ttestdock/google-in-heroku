import os
from wsgiref.simple_server import make_server
import urllib2
def application(environ,start_response):
    #response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]
    #response_body = '\n'.join(response_body)
    try:
        url=str(environ["PATH_INFO"])+"?"+str(environ["QUERY_STRING"])
    except:
        url=="http://translate.google.com"
    google="http://translate.google.com"
    res=urllib2.urlopen(google+url)
    html=res.read()
    status='200 OK'
    response_headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(html)))]
    start_response(status, response_headers)

    return html

port=int(os.environ.get("PORT",5000))
httpd=make_server('0.0.0.0',port,application)
httpd.serve_forever()


