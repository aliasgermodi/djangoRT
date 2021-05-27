from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):

        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # await self.disconnect()
        pass
    
    async def receive(self, text_data):
        
        print(">>>>", text_data)

        pass

class Notification(AsyncWebsocketConsumer):
    
    async def connect(self):

        self.groupname = 'notification'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # await self.disconnect()
        pass
    
    async def receive(self, text_data):
        
        print("This is Notification : ", text_data)

        pass