#!/usr/bin/env python
#
#    Copyright (c)2016 Jason Noorman.
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files (the "Software"),
#    to deal in the Software without restriction, including without limitation
#    the rights to use, copy, modify, merge, publish, distribute, sublicense,
#    and/or sell copies of the Software, and to permit persons to whom the Software
#    is furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#    ------------------------------------------------------------------------------
#
#    Note: You may require the 'requests[security]' package to correctly handle the
#          SSL connection depending on your version of python.
#

import requests
import json

# Obtain these keys from the Telstra Developer Portal - https://dev.telstra.com

consumer_key    = "your_consumer_key"
consumer_secret = "your_consumer_secret"

def send_SMS(sms_number, sms_message):
	#print "Sending SMS"
	r=requests.post("https://api.telstra.com/v1/oauth/token",
    		headers={'content-type':'application/x-www-form-urlencoded'},
    		data={'client_id':str(consumer_key), 'client_secret':str(consumer_secret), 'grant_type':'client_credentials', 'scope':'SMS'})

	data=r.json()

	url = 'https://api.telstra.com/v1/sms/messages'
	headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % str(data["access_token"])}
	payload = json.dumps({'to': str(sms_number), 'body': str(sms_message)})

	w=requests.post(url, headers=headers, data=payload)
   	
	return

send_SMS('number_to_sms','Your message')
