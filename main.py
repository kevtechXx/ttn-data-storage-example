import requests
import json
import base64

r = requests.get("https://appname.data.thethingsnetwork.org/api/v2/query",
    headers={
        "Accept": "application/json",
        "Authorization": "key yourappkey", # Replace yourappkey with your app key
    }
).json()

for i in r:
    print("\n--- Message ---")
    print("Device ID: {}".format(i["device_id"]))
    print("Message: {}".format(base64.b64decode(i["raw"]).decode()))
