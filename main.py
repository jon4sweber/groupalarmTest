#!/usr/bin/python3

import requests
import os
import json

URL = "https://app.groupalarm.com/api/v1/alarms/user"
KEY = os.getenv("API_KEY")
ORG_ID = "14416"

headers = {
    "Personal-Access-Token": KEY,
}
params = {
    "organization": ORG_ID
}
def get_response():
    response = requests.get(url=URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

data = get_response()
print(data)
if data["alarms"] == []:
    print("no alarm")
else:
    with open("alarm.log", "a") as log_file:
        json.dump(obj=data, fp=log_file, indent=2)
        log_file.close()