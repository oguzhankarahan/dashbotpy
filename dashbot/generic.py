from __future__ import print_function

import sys
import requests
import json
import traceback
import os
import logging

class DashBotGeneric():
    
    def __init__(self,apiKey=None,debug=True,printErrors=True):
        
        if 'DASHBOT_SERVER_ROOT' in os.environ:
            serverRoot = os.environ['DASHBOT_SERVER_ROOT']
        else:
            serverRoot = 'https://tracker.dashbot.io'        
        self.urlRoot = serverRoot + '/track'        
        self.apiKey=apiKey
        self.debug=debug
        self.printErrors=printErrors
        self.platform='alexa'
        self.version = '0.0.1'
        self.source = 'pip'
        
    def getBasestring(self):
        if (sys.version_info > (3, 0)):
            return (str, bytes)
        else:
            return basestring        

    def makeRequest(self,url,method,json):
        try:
            if method=='GET':
                r = requests.get(url, params=json)
            elif method=='POST':
                r = requests.post(url, json=json)
            else:
                print('Error in makeRequest, unsupported method')
            if self.debug:
                print('dashbot response')
                print (r.text)
            if r.status_code!=200:
                logging.error("ERROR: occurred sending data. Non 200 response from server:"+str(r.status_code))
        except ValueError as e:
            logging.error("ERROR: occurred sending data. Exception:",str(e))