#/usr/bin/python
import ciscospark
import clickatelsms
import gmailsendmail


#How to use
#call using
#message = "message from python interpreter"
#notify.notify(message)

def notify(message):
  print "Sending Message via Clickatell SMS"
  clickatelsms.sendSMS(message)
  print "Sending Message to Cisco Spark"
  ciscospark.sendSpark(message)
  print "Sending Message via Gmail"
  gmailsendmail.sendGmail(message)
