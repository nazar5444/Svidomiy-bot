from sseclient import SSEClient
import json

url = "https://alerts.com.ua/api/states/live"
headers = {"X-API-Key": "5ebcb2ed4d4fd3d565a3d4ae028c0242c5e583d8"}

messages = SSEClient(url, headers=headers)

for msg in messages:
    if msg.event == "update":
        data = json.loads(msg.data)
        state = data["state"]
        print("State ID:", state["id"])
        print("State Name:", state["name"])
        print("Alert:", state["alert"])
    if msg.event == "hello":
        print("hello")
