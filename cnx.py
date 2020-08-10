import RPi.GPIO as GPIO          
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

cred = credentials.Certificate("/home/pi/PFE/surfrobot-e5d15-firebase-adminsdk-82oph-a8a85f526b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://surfrobot-e5d15.firebaseio.com/'
})
def moto ():
	Arierre = db.reference('moteur/Arierre').get()
	print(Arierre)
	Avant = db.reference('moteur/Avant').get()
	print(Avant)
	Droite = db.reference('Direction/Droite').get()
	print(Droite) 
	Gauche = db.reference('Direction/Gauche').get()
	print(Gauche)
	toutdroit = db.reference('Direction/toutdroit').get()
	print(toutdroit) 
	servx = db.reference('Camera/servx').get()
	print(servx)	


								
moto()
