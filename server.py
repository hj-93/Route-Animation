#!/usr/bin/env python

import asyncio
import websockets

async def serving(websocket, path):
    while True:
        index = random.randint(0,8)
        await websocket.send(str(coords[index][0]) + "," + str(coords[index][1]))

start_server = websockets.serve(serving, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

coords = [
    (
        57.694132,
        11.935906
    ),
    (
        57.680244,
        11.927149
    ),
    (
        57.640720,
        12.041243
    ),
    (
        57.794132,
        11.938906
    ),
    (
        57.688244,
        11.925149
    ),
    (
        57.643720,
        12.046243
    ),
        (
        57.694132,
        11.936906
    ),
    (
        57.685244,
        11.927149
    ),
    (
        57.645720,
        12.041243
    )
]
