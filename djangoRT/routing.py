# from channels.routing import ProtocolTypeRouter,URLRouter
# from channels.auth import AuthMiddlewareStack

# from django.urls import path
# from firstPage import consumer

# websocket_urlPattern=[
#     path('ws/polData/',consumer.DashConsumer.as_asgi()),
#     path('ws/Notify/',consumer.Notification.as_asgi()),
# ]

# application=ProtocolTypeRouter({
#     # 'http':
#     'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

# })
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# Importing notification Consumer from consumers.py
from firstPage.consumers import NotificationConsumer


websocket_urlPattern = [
    path('notifications/', NotificationConsumer.as_asgi()),
    path('add_person/', NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    # Websocket chat handler
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})
