import json

from aiohttp_sse_client import client as sse_client

import db


async def alertlive_func():
    headers = {"X-API-Key": "5ebcb2ed4d4fd3d565a3d4ae028c0242c5e583d8"}
    async with sse_client.EventSource(
            'https://alerts.com.ua/api/states/live',
            headers=headers
    ) as event_source:
        try:
            async for event in event_source:
                if event.type == "hello":
                    print(event.data)
                if event.type == "update":
                    data = json.loads(event.data)
                    state = data["state"]
                    print("State ID:", state["id"])
                    print("Alert:", state["alert"])
                    print(event)
                    res = db.cur.execute("SELECT user_id FROM users WHERE city_id=%s", (state["id"],))
                    id_list_changes = db.cur.fetchall()
                    for user_id in id_list_changes:
                        if state["alert"] is False:
                            print(user_id[0], 'Відбій повітряної тривоги')
                        elif state["alert"] is True:
                            print(user_id[0], 'Повітряна тривога')
        except ConnectionError:
            pass
