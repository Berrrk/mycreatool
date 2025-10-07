"""
MyCreatool - Kullanıcı Yönetimi URL Yapılandırması

Bu dosya kullanıcı yönetimi API endpoint'lerinin URL yönlendirmelerini içerir.
Tüm endpoint'ler JWT token tabanlı kimlik doğrulama kullanır.

API Endpoint'leri:
- POST /api/accounts/register/     : Yeni kullanıcı kaydı
- POST /api/accounts/login/        : Kullanıcı girişi (JWT token)
- POST /api/accounts/token/refresh/ : JWT token yenileme
- GET  /api/accounts/profile/      : Kullanıcı profil bilgileri

Güvenlik:
- JWT token tabanlı kimlik doğrulama
- Rate limiting
- CORS desteği
"""
from django.urls import path
from .views import RegisterView, ProfileView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Kullanıcı kaydı endpoint'i
    path('register/', RegisterView.as_view(), name='register'),
    
    # Kullanıcı girişi endpoint'i (JWT token)
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT token yenileme endpoint'i
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Kullanıcı profil bilgileri endpoint'i
    path('profile/', ProfileView.as_view(), name='profile'),
]
