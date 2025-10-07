"""
MyCreatool Projesi - ASGI Yapılandırması

Bu dosya Django projesinin ASGI (Asynchronous Server Gateway Interface) yapılandırmasını içerir.
Asenkron işlemler, WebSocket bağlantıları ve real-time özellikler için kullanılır.

ASGI Nedir:
- Asenkron Python web uygulamaları için arayüz
- WebSocket, HTTP/2, Server-Sent Events desteği
- Real-time uygulamalar için ideal

Kullanım:
- Django Channels ile WebSocket
- Asenkron view'lar
- Real-time bildirimler
- Chat uygulamaları
"""
import os

from django.core.asgi import get_asgi_application

# Django settings modülünü ayarla
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycreatool.settings')

# ASGI application objesini oluştur
application = get_asgi_application()
