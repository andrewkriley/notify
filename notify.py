#/usr/bin/python
#import cisco-spark
import clickatelsms
#import gmail-sendmail

message = "hello world"

def notify(message):
  clickatelsms.sendSMS(message)
  #cisco-spark(message)
  #gmail-sendmail(message)

notify(message)
