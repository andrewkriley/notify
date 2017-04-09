# notify
A notify engine that takes a message and sends to Clickatel SMS, Cisco Spark and Gmail

rename config.py.sample to config.py
change the following parameters

Then import notify into your own function by calling notify(message)
where message is your string

call using

message = "hello world this message will be send via SMS Spark and GMAIL"
notify.notify(message)
