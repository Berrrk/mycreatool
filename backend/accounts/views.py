"""
MyCreatool - Kullanıcı Yönetimi API Görünümleri

Bu dosya kullanıcı kaydı, girişi ve profil yönetimi için API endpoint'lerini içerir.
JWT token tabanlı kimlik doğrulama sistemi kullanılır.

API Endpoint'leri:
- POST /api/accounts/register/     : Kullanıcı kaydı
- POST /api/accounts/login/        : Kullanıcı girişi (JWT token)
- GET  /api/accounts/profile/      : Kullanıcı profil bilgileri

Güvenlik Özellikleri:
- JWT token tabanlı kimlik doğrulama
- CORS desteği
- Rate limiting
- Input validation
"""
from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    """
    Kullanıcı Kayıt API Endpoint'i
    
    Yeni kullanıcı kaydı oluşturur.
    Davet kodu doğrulaması yapar.
    
    HTTP Method: POST
    Permission: AllowAny (herkes erişebilir)
    
    Request Body:
        {
            "email": "user@example.com",
            "password": "securepassword",
            "invite_code": "invite-code-uuid"
        }
    
    Response:
        {
            "message": "Kullanıcı başarıyla oluşturuldu",
            "user": {
                "email": "user@example.com",
                "username": null,
                "credits": 0
            }
        }
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
    """
    JWT Token Alma API Endpoint'i
    
    Kullanıcı girişi yapar ve JWT token döner.
    Access token ve refresh token çifti sağlar.
    
    HTTP Method: POST
    Permission: AllowAny (herkes erişebilir)
    
    Request Body:
        {
            "email": "user@example.com",
            "password": "securepassword"
        }
    
    Response:
        {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
            "user": {
                "email": "user@example.com",
                "username": null,
                "credits": 0
            }
        }
    """
    serializer_class = MyTokenObtainPairSerializer

class ProfileView(APIView):
    """
    Kullanıcı Profil Bilgileri API Endpoint'i
    
    Kimlik doğrulaması yapılmış kullanıcının profil bilgilerini döner.
    Kredi miktarı ve diğer kullanıcı bilgilerini içerir.
    
    HTTP Method: GET
    Permission: IsAuthenticated (sadece giriş yapmış kullanıcılar)
    
    Headers:
        Authorization: Bearer <access_token>
    
    Response:
        {
            "email": "user@example.com",
            "username": "kullanici_adi",
            "credits": 100
        }
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Kullanıcının profil bilgilerini döner
        
        Args:
            request: HTTP request objesi (authenticated user içerir)
            
        Returns:
            Response: JSON formatında kullanıcı bilgileri
        """
        user = request.user
        data = {
            "email": user.email,
            "username": user.username,
            "credits": user.credits,
        }
        return Response(data)
