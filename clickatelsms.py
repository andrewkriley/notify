#/usr/bin/python

# To call from other function

            #import clickatelsms

            #message = "hello world"

            #def sms(message):
            #  clickatelsms.sendSMS(message)

            #sms(message)

import urllib2
import config

def sendSMS(message):

    #Clickatell Account Details
    #Format message to remove spaces and replace with %20 to suit URL formatting before sending
    sms = message.replace(" ", "%20")
    print(sms)

    #URL
    urlComplete = "http://api.clickatell.com/http/sendmsg?user=" + config.clickatellUser + "&password=" + config.clickatellPassword + "&api_id=" + config.clickatellAPI + "&to=" + config.smsRecipient + "&text=" + sms

    print(urlComplete)

    #Send Message
    response = urllib2.urlopen(urlComplete)
    html = response.read()
    print(html)
