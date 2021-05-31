# from django.shortcuts import render
# from django.http import JsonResponse
# import websocket
# import json
# import asyncio

# # Create your views here.

# ws = websocket.WebSocket()
# # ws = websocket.WebSocket('ws://localhost:8000/ws/polData/')

# def index(request):
#     return render(request, 'index.html')

# def notify(request):

#     return render(request, 'notify.html')

#     # timeout = 5
#     # loop = asyncio.new_event_loop()
#     # asyncio.set_event_loop(loop)

#     # ws.connect('ws://localhost:8000/ws/Notify/')
#     # ws.send(json.dumps('Hello'))
#     # ws_conn = loop.run_until_complete(ws.connect('ws://localhost:8000/ws/polData/'), timeout)
#     # loop.run_until_complete(ws_conn.send(json.dumps("Hello Notifiy")))

#     # response = loop.run_until_complete(ws_conn.recv())
#     # ws_conn.close()

#     # return JsonResponse({'some': 'data'})

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from datetime import datetime
from django.shortcuts import render, redirect
import time
# Create your views here.


# Basic home view
def home(request):
    return render(request, 'home.html')


# Django Channels


def notification_test_page(request):

    # Django Channels Notifications Test
    current_user = request.user
    print(current_user)
    channel_layer = get_channel_layer()
    data = "notification" + "...." + str(datetime.now())
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )
    # requests.get("http://localhost:8000/add_person_notify/")
    return render(request, 'notifications_test_page.html')
    # time.sleep(3)
    # return redirect('http://127.0.0.1:8000/add_person_notify/')


def add_person(request):
    current_user = request.user
    channel_layer = get_channel_layer()
    data = "notification" + "...." + "New person added"
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )
    print("success")
    time.sleep(3)
    return redirect('http://127.0.0.1:8000/notifications-test/')
