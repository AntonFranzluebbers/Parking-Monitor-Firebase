from firebase import Firebase
from firebase_token_generator import create_token
import time
import random


auth_payload = {"uid":"k6wJ1M33MnaTiuRGU5IrFTwM5H53"}
token = create_token("1ufUtMReQxZlUe8kHdCs2WDfcmWdDKNeIziMg49o", auth_payload)


for i in range (1,100):

	spotId = random.randrange(1,127)
	f = Firebase("https://parking-monitor.firebaseio.com/lots/S17", auth_token=token)
	distance = random.randrange(0,400)
	randTime = random.randrange(1435255107,1465265107)
	rp = f.post({"date":randTime, "serial":"HC-SR04-1", "distance":distance, "spot":spotId})
	print("POST: " + str(rp))
	time.sleep(1)
