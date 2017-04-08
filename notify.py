#/usr/bin/python
#import cisco-spark
import clickatelsms
#import gmail-sendmail

message = "hello world"

def main(message):
  clickatelsms.sendSMS(message)
  #cisco-spark(message)
  #gmail-sendmail(message)

main(message)
