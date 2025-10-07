"""
MyCreatool Projesi - WSGI Yapılandırması

Bu dosya Django projesinin WSGI (Web Server Gateway Interface) yapılandırmasını içerir.
Production sunucularında (Apache, Nginx) Django uygulamasını çalıştırmak için kullanılır.

WSGI Nedir:
- Python web uygulamaları ile web sunucuları arasındaki arayüz
- HTTP isteklerini Django'ya yönlendirir
- Production deployment için gerekli

Kullanım:
- Apache mod_wsgi ile
- Nginx + uWSGI/Gunicorn ile
- Docker container'larında
"""
import os

from django.core.wsgi import get_wsgi_application

# Django settings modülünü ayarla
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycreatool.settings')

# WSGI application objesini oluştur
application = get_wsgi_application()
