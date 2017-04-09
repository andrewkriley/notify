#/usr/bin/python
import ciscospark
import clickatelsms
#import gmail-sendmail

message = "hello world from Notify"

def notify(message):
  clickatelsms.sendSMS(message)
  ciscospark.sendSpark(message)
  #gmail-sendmail(message)

notify(message)
