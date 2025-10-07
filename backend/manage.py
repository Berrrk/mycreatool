#!/usr/bin/env python
"""
Django Yönetim Aracı - MyCreatool Projesi

Bu dosya Django projesinin komut satırından yönetilmesi için kullanılır.
Proje yöneticileri bu araç ile:
- Veritabanı migration'larını çalıştırabilir
- Superuser oluşturabilir
- Django shell'ini başlatabilir
- Proje testlerini çalıştırabilir

Kullanım:
    python manage.py migrate          # Veritabanı güncellemeleri
    python manage.py createsuperuser  # Admin kullanıcı oluşturma
    python manage.py runserver        # Geliştirme sunucusu başlatma
    python manage.py shell            # Django shell
"""
import os
import sys


def main():
    """
    Django yönetim komutlarını çalıştırır.
    
    Bu fonksiyon:
    1. Django settings modülünü ayarlar
    2. Django'yu import eder
    3. Komut satırı argümanlarını işler
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycreatool.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
