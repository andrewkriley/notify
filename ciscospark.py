#usr/bin/python

import json
import requests
import config

ACCESS_TOKEN = config.ciscoSparkToken #put your access token between the quotes.
ROOM_NAME    = config.ciscoSparkRoomName #put the name of a room to which you belong between the quotes.
#message = "test from this file"

def setHeaders():
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return spark_header


def getRooms(theHeader):
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.get(uri, headers=theHeader)
	return resp.json()

def findRoom(roomList,name):
	roomId=0
	for room in roomList["items"]:
		if room["title"] == name:
			roomId=room["id"]
			break
	return roomId

def addMessageToRoom(theHeader,roomID,message):
	uri = "https://api.ciscospark.com/v1/messages"
	payload= {"roomId":roomID,"text":message}
	resp = requests.post(uri, data=json.dumps(payload), headers=theHeader)
	return resp.json()

def sendSpark(message):
    header=setHeaders()
    rooms=getRooms(header)
    roomID=findRoom(rooms,ROOM_NAME)
    if roomID != 0:
    	resp=addMessageToRoom(header,roomID,message)
        print ROOM_NAME + " " + roomID
        print message
    else:
    	print("Specified room was not found!")

#sendSpark(message)
