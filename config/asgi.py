# config/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# *** CRUCIAL: Import your app's routing file ***
import chat.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app, 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # *** CRUCIAL: Reference the correct list of URL patterns ***
            chat.routing.websocket_urlpatterns 
        )
    ),
})