import os
from wsgiref.simple_server import make_server
import urllib2
def application(environ,start_response):

    googleUrl="https://scholar.google.com"

    try:
        userAgent=str(environ["HTTP_USER_AGENT"])
        requestUrl=str(environ["PATH_INFO"])+"?"+str(environ["QUERY_STRING"])
        httpAccept=str(environ["HTTP_ACCEPT"]) 
    except:
        userAgent="Mozilla/5.0"
        requestUrl=""


    try:
        opener=urllib2.build_opener()
        opener.addheaders=[('User-agent', userAgent)]
        opener.addheaders=[('Accept',httpAccept)]
        html=opener.open(googleUrl+requestUrl).read()
    except:
        html="Can not open the page.Please retry in a few minutes"

    status='200 OK'
    response_headers = [('Content-Type', 'text/html;charset=utf-8'),('Content-Length', str(len(html)))]
    start_response(status, response_headers)

    return html

port=int(os.environ.get("PORT",5000))
httpd=make_server('0.0.0.0',port,application)
httpd.serve_forever()


