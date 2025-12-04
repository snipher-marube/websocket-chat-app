# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # This is called when the WebSocket is handshaked and accepted.
        self.accept()
        print("WebSocket Connected!")

        # Send an immediate message to the client for confirmation
        self.send(text_data=json.dumps({
            'message': 'Welcome! Connection successful.'
        }))

    def disconnect(self, close_code):
        # This is called when the WebSocket is closed.
        print(f"WebSocket Disconnected! Code: {close_code}")
        pass

    def receive(self, text_data):
        # This is called when a message is received from the client.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(f"Received message: {message}")

        # Echo the received message back to the same client
        self.send(text_data=json.dumps({
            'message': f"You said: {message}"
        }))