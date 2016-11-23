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
