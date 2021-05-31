import json
import requests
import redis
import websocket

ws = websocket.WebSocket()
ws2 = websocket.WebSocket()

import random, time

# ws.connect('ws://localhost:8000/ws/polData/')
# ws2.connect('ws://localhost:8000/ws/Notify/')
ws.connect('ws://localhost:8000/notifications/')

# for i in range(1000):
#     time.sleep(3)

#     ws.send(json.dumps({'value':random.randint(1,1000)}))
ws.send(json.dumps({'value':"Hello Notifiy"}))
# ws2.send(json.dumps({'value':"Hello Notifiy2"}))