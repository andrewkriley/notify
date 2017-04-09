#/usr/bin/python

import smtplib
import config

def sendGmail(message):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.username,config.password)
    server.sendmail(config.fromaddr, config.toaddrs, message)
    server.quit()

#sendGmail(message)
