import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/home/pi/PFE/surfrobot-e5d15-firebase-adminsdk-82oph-a8a85f526b.json")
firebase_admin.initialize_app(cred)

