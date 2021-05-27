from django.shortcuts import render
from django.http import JsonResponse
import websocket
import json
import asyncio

# Create your views here.

ws = websocket.WebSocket()
# ws = websocket.WebSocket('ws://localhost:8000/ws/polData/')

def index(request):
    return render(request, 'index.html')

def notify(request):

    return render(request, 'notify.html')

    # timeout = 5
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)

    # ws.connect('ws://localhost:8000/ws/Notify/')
    # ws.send(json.dumps('Hello'))
    # ws_conn = loop.run_until_complete(ws.connect('ws://localhost:8000/ws/polData/'), timeout)
    # loop.run_until_complete(ws_conn.send(json.dumps("Hello Notifiy")))

    # response = loop.run_until_complete(ws_conn.recv())
    # ws_conn.close()

    # return JsonResponse({'some': 'data'})