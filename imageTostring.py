import base64
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import datetime
import sys
import time
import subprocess

cred = credentials.Certificate("/home/pi/PFE/surfrobot-e5d15-firebase-adminsdk-82oph-a8a85f526b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://surfrobot-e5d15.firebaseio.com/'
})

# read the absolute path
script_dir = os.path.dirname(__file__)

while (1):
#CAPTURE IMAGE
	# call the .sh to capture the image
	os.system('/home/pi/PFE/webcam/webcam.sh')
	#  join the absolute path and created file name
	abs_file_path = os.path.join(script_dir,"2019.jpg")
	print(1)
#CONVERT IMAGE TO BASE64 AND SEND TO DATABASE
	with open("/home/pi/PFE/webcam/2019.jpg", "rb") as imageFile:
		db.reference('/').update({
		'image': "data:image/jpg;base64,"+base64.b64encode(imageFile.read())
	})
