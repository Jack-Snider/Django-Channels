"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter

import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 변수는 default로 application으로 되있겠지만 django_asgi_app로 변경
django_asgi_app = get_asgi_application() 

application = ProtocolTypeRouter({
    "http" : django_asgi_app, 
    "websocket" : URLRouter(
        app.routing.websocket_urlpatterns
    ),
})
