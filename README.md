# notify
A notify engine that takes a message and sends to Clickatel SMS, Cisco Spark and Gmail

rename config.py.sample to config.py
change the following parameters

#Cisco Spark parameters
ciscoSparkToken = ""
ciscoSparkRoomId = ""

#Click-a-Tell parameters
clickatellUser = ""
clickatellPassword = ""
clickatellAPI = ""
smsRecipient = ""

#GMAIL
gmailUser = ""
gmailPass = ""

Then import notify into your own function by calling notify(message)
where message is your string
