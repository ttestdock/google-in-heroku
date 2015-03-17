import os
from wsgiref.simple_server import make_server
import urllib2
def application(environ,start_response):
    #response_body = ['%s: %s' % (key, value) for key, value in sorted(environ.items())]
    #response_body = '\n'.join(response_body)
    try:
        requestUrl=str(environ["PATH_INFO"])+"?"+str(environ["QUERY_STRING"])
    except:
        return "Error!"
    
    try:
        userAgent=str(environ["HTTP_USER_AGENT"])
    except:
        userAgent="Mozilla/5.0"

    googleUrl="https://www.google.com"
    
    try:
        opener=urllib2.build_opener()
        opener.addheaders=[('User-agent', userAgent)]
        html=opener.open(googleUrl+requestUrl).read()
    except:
        html="something wrong"
    
    status='200 OK'
    response_headers = [('Content-Type', 'text/html;charset=utf-8'),('Content-Length', str(len(html)))]
    start_response(status, response_headers)

    return html

port=int(os.environ.get("PORT",5000))
httpd=make_server('0.0.0.0',port,application)
httpd.serve_forever()


