"""
MyCreatool Projesi - Ana URL Yapılandırması

Bu dosya projenin tüm URL yönlendirmelerini yönetir.
Her URL isteği burada tanımlanan pattern'lere göre ilgili view'lere yönlendirilir.

URL Yapısı:
- /admin/           : Django admin paneli
- /api/accounts/    : Kullanıcı işlemleri API'si (kayıt, giriş, profil)
- /api/imagegen/    : Görsel üretimi API'si
- /imagegen/        : Görsel üretimi web arayüzü

Güvenlik Notu:
- Tüm API endpoint'leri JWT token ile korunmaktadır
- Admin paneli superuser yetkisi gerektirir
- CORS ayarları frontend erişimi için yapılandırılmıştır
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Paneli - Sistem yönetimi için
    # Superuser yetkisi gerektirir
    path('admin/', admin.site.urls),
    
    # Görsel Üretimi Web Arayüzü - Kullanıcılar için web interface
    # AI tabanlı görsel üretimi araçları
    path('imagegen/', include('imagegen.urls')),
    
    # Kullanıcı Yönetimi API'si - RESTful API endpoint'leri
    # Kullanıcı kaydı, girişi, profil yönetimi
    path('api/accounts/', include('accounts.urls')),
    
    # Görsel Üretimi API'si - Programatik erişim için
    # Mobil uygulamalar ve üçüncü parti entegrasyonlar
    path('api/imagegen/', include('imagegen.urls')),
]
