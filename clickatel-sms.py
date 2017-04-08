#/usr/bin/python

def sendSMS():
    #Format message to remove spaces and replace with %20 to suit URL formatting before sending
    sms = smsInputMessage.replace(" ", "%20")
    print(sms)

    #URL
    urlComplete = 'http://api.clickatell.com/http/sendmsg?user={0}&password={1}&api_id={2}&to={3}&text={4}'.format(clickatellUser, clickatellPassword, clickatellAPI, smsRecipient, sms
)
    print(urlComplete)

    #Send Message
    response = urllib2.urlopen(urlComplete)
    html = response.read()
    print(html)
