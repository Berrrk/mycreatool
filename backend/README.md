# 🚀 MyCreatool Backend - Django API

<div align="center">

![Django](https://img.shields.io/badge/Django-5.1.13-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.16.1-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

**Modern Django REST API - AI Powered Creative Solutions**

</div>

---

## 📋 İçindekiler

- [🎯 Backend Hakkında](#-backend-hakkında)
- [🏗️ Mimari](#️-mimari)
- [📁 Proje Yapısı](#-proje-yapısı)
- [🚀 Kurulum](#-kurulum)
- [🔧 Geliştirme](#-geliştirme)
- [📚 API Endpoints](#-api-endpoints)
- [🤖 AI Entegrasyonu](#-ai-entegrasyonu)
- [🔐 Güvenlik](#-güvenlik)
- [📊 Veritabanı](#-veritabanı)
- [🧪 Test](#-test)
- [🚀 Deployment](#-deployment)

---

## 🎯 Backend Hakkında

**MyCreatool Backend**, Django REST Framework kullanılarak geliştirilmiş modern bir API servisidir. AI tabanlı görsel işleme, kullanıcı yönetimi ve güvenli kimlik doğrulama sistemleri içerir.

### ✨ Temel Özellikler
- 🔐 **JWT Token Authentication** - Güvenli API erişimi
- 👥 **Custom User Model** - Email tabanlı kimlik doğrulama
- 🎨 **AI Image Processing** - Görsel üretimi ve düzenleme
- 🎫 **Invite Code System** - Beta erişim kontrolü
- 📊 **Credit System** - Adil kullanım yönetimi
- 🐳 **Docker Ready** - Containerized deployment

---

## 🏗️ Mimari

### 📊 Teknoloji Stack

```
┌─────────────────────────────────────────┐
│                Frontend                 │
│           React + Vite                  │
└─────────────────┬───────────────────────┘
                  │ HTTP/HTTPS
                  │ JWT Authentication
┌─────────────────▼───────────────────────┐
│               Backend API               │
│        Django REST Framework           │
├─────────────────────────────────────────┤
│  • User Management (accounts)          │
│  • AI Image Processing (imagegen)      │
│  • Authentication & Authorization      │
│  • Business Logic                      │
└─────────────────┬───────────────────────┘
                  │ ORM Queries
┌─────────────────▼───────────────────────┐
│              Database                   │
│         PostgreSQL (Neon)              │
└─────────────────────────────────────────┘
```

### 🔄 Request Flow

```
1. Frontend Request → 2. Django Middleware → 3. URL Routing → 
4. View Processing → 5. Serializer Validation → 6. Model Operations → 
7. Database Query → 8. Response Serialization → 9. JSON Response
```

---

## 📁 Proje Yapısı

```
backend/
├── 📁 accounts/                    # Kullanıcı Yönetimi Modülü
│   ├── 📄 models.py               # CustomUser, InviteCode modelleri
│   ├── 📄 views.py                # API endpoint'leri
│   ├── 📄 serializers.py          # Veri doğrulama
│   ├── 📄 urls.py                 # URL routing
│   ├── 📄 admin.py                # Django admin paneli
│   ├── 📄 apps.py                 # App konfigürasyonu
│   └── 📁 migrations/             # Veritabanı migration'ları
├── 📁 imagegen/                   # AI Görsel İşleme Modülü
│   ├── 📄 models.py               # Image, Generation modelleri
│   ├── 📄 views.py                # AI processing endpoint'leri
│   ├── 📄 serializers.py          # AI request/response
│   ├── 📄 urls.py                 # AI URL routing
│   ├── 📄 admin.py                # AI admin paneli
│   └── 📁 templates/              # AI web arayüzü
├── 📁 mycreatool/                 # Ana Proje Konfigürasyonu
│   ├── 📄 settings.py             # Django ayarları
│   ├── 📄 urls.py                 # Ana URL routing
│   ├── 📄 wsgi.py                 # WSGI konfigürasyonu
│   └── 📄 asgi.py                 # ASGI konfigürasyonu
├── 📄 manage.py                   # Django yönetim aracı
├── 📄 requirements.txt            # Python bağımlılıkları
├── 📄 Dockerfile                  # Backend container
├── 📄 .env                        # Environment variables
└── 📄 README.md                   # Bu dosya
```

---

## 🚀 Kurulum

### 📋 Gereksinimler

- **Python**: 3.10+
- **Docker**: 20.10+
- **PostgreSQL**: Neon (Cloud) veya Local
- **Git**: 2.30+

### ⚡ Docker ile Kurulum

#### 1. Projeyi Klonlayın
```bash
git clone https://github.com/yourusername/mycreatool.git
cd mycreatool/backend
```

#### 2. Environment Variables
```bash
# .env dosyası oluşturun
cp .env.example .env

# .env dosyasını düzenleyin
DATABASE_URL=postgresql://username:password@host:port/database
SECRET_KEY=your-super-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 3. Docker ile Çalıştırın
```bash
# Ana proje klasöründen
docker-compose build backend
docker-compose up backend

# Veya sadece backend
docker build -t mycreatool-backend .
docker run -p 8000:8000 mycreatool-backend
```

#### 4. Veritabanı Kurulumu
```bash
# Migration'ları çalıştır
docker-compose exec backend python manage.py migrate

# Superuser oluştur
docker-compose exec backend python manage.py createsuperuser

# Static dosyaları topla
docker-compose exec backend python manage.py collectstatic
```

### 🔧 Manuel Kurulum

#### 1. Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

#### 2. Bağımlılıkları Kurun
```bash
pip install -r requirements.txt
```

#### 3. Veritabanı Ayarları
```bash
# PostgreSQL kurulumu (Ubuntu)
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres createdb mycreatool

# Migration'ları çalıştır
python manage.py migrate
```

#### 4. Geliştirme Sunucusu
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 🔧 Geliştirme

### 🛠️ Geliştirme Komutları

#### Django Management
```bash
# Migration oluştur
python manage.py makemigrations

# Migration uygula
python manage.py migrate

# Django shell
python manage.py shell

# Testleri çalıştır
python manage.py test

# Admin kullanıcısı oluştur
python manage.py createsuperuser

# Static dosyaları topla
python manage.py collectstatic
```

#### Docker Development
```bash
# Container'a bağlan
docker-compose exec backend bash

# Logları takip et
docker-compose logs -f backend

# Container'ı yeniden başlat
docker-compose restart backend

# Yeni paket ekle
docker-compose exec backend pip install package-name
```

### 📝 Kod Standartları

#### Python Style Guide
```python
# ✅ İyi örnek
class CustomUserManager(BaseUserManager):
    """
    Özelleştirilmiş Kullanıcı Yöneticisi
    
    Django'nun varsayılan kullanıcı modelini genişletir.
    Email tabanlı kimlik doğrulama sistemi sağlar.
    """
    
    def create_user(self, email: str, password: str = None, **extra_fields) -> 'CustomUser':
        """
        Normal kullanıcı oluşturur
        
        Args:
            email: Kullanıcı email adresi (zorunlu)
            password: Kullanıcı şifresi
            **extra_fields: Ek kullanıcı bilgileri
            
        Returns:
            CustomUser: Oluşturulan kullanıcı objesi
        """
        if not email:
            raise ValueError('Users must have an email address!')
        # ... implementation
```

#### API Response Format
```python
# ✅ Standart API response
{
    "success": True,
    "message": "İşlem başarılı",
    "data": {
        "user": {
            "email": "user@example.com",
            "username": "kullanici_adi",
            "credits": 100
        }
    },
    "timestamp": "2025-01-06T20:30:00Z"
}

# ❌ Hata response
{
    "success": False,
    "message": "Geçersiz davet kodu",
    "errors": {
        "invite_code": ["Bu davet kodu zaten kullanılmış."]
    },
    "timestamp": "2025-01-06T20:30:00Z"
}
```

---

## 📚 API Endpoints

### 🔐 Kimlik Doğrulama

#### Kullanıcı Kaydı
```http
POST /api/accounts/register/
Content-Type: application/json

{
    "email": "user@example.com",
    "username": "kullanici_adi",
    "password": "securepassword",
    "password2": "securepassword",
    "invite_code": "invite-code-uuid",
    "profile_image": "<file>"
}

Response:
{
    "success": True,
    "message": "Kullanıcı başarıyla oluşturuldu",
    "data": {
        "user": {
            "email": "user@example.com",
            "username": "kullanici_adi",
            "credits": 0
        }
    }
}
```

#### Giriş (JWT Token)
```http
POST /api/accounts/login/
Content-Type: application/json

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
        "username": "kullanici_adi",
        "credits": 100
    }
}
```

#### Token Yenileme
```http
POST /api/accounts/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

Response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Profil Bilgileri
```http
GET /api/accounts/profile/
Authorization: Bearer <access_token>

Response:
{
    "email": "user@example.com",
    "username": "kullanici_adi",
    "credits": 100
}
```

### 🎨 AI Görsel İşleme

#### Görsel Üretimi
```http
POST /api/imagegen/generate/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "prompt": "A beautiful sunset over mountains",
    "language": "tr",
    "style": "photorealistic",
    "quality": "high",
    "dimensions": "1024x1024"
}

Response:
{
    "success": True,
    "message": "Görsel üretimi başlatıldı",
    "data": {
        "task_id": "uuid-task-id",
        "status": "processing",
        "estimated_time": 30
    }
}
```

#### Görsel Düzenleme
```http
POST /api/imagegen/edit/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
    "image": <file>,
    "edit_prompt": "Make it more colorful and vibrant",
    "operation": "enhance",
    "intensity": 0.7
}

Response:
{
    "success": True,
    "message": "Görsel düzenleme başlatıldı",
    "data": {
        "task_id": "uuid-task-id",
        "status": "processing"
    }
}
```

#### İşlem Durumu Sorgulama
```http
GET /api/imagegen/task/{task_id}/
Authorization: Bearer <access_token>

Response:
{
    "success": True,
    "data": {
        "task_id": "uuid-task-id",
        "status": "completed",
        "result": {
            "image_url": "https://cdn.example.com/generated-image.jpg",
            "thumbnail_url": "https://cdn.example.com/thumbnail.jpg",
            "metadata": {
                "prompt": "A beautiful sunset over mountains",
                "processing_time": 25.3,
                "credits_used": 5
            }
        }
    }
}
```

---

## 🤖 AI Entegrasyonu

### 🎯 AI Görsel Üretimi

#### Prompt İşleme
```python
# Çok dilli prompt desteği
def process_prompt(prompt: str, language: str = "en") -> str:
    """
    Prompt'u AI için optimize eder
    
    - Çok dilli destek
    - Prompt iyileştirme
    - Güvenlik filtreleme
    """
    # Dil tespiti ve çeviri
    if language != "en":
        prompt = translate_prompt(prompt, target_language="en")
    
    # Prompt iyileştirme
    optimized_prompt = optimize_prompt_for_ai(prompt)
    
    return optimized_prompt
```

#### AI Service Integration
```python
# AI servis entegrasyonu
class AIImageGenerator:
    """
    AI görsel üretimi servisi
    
    - Çoklu AI provider desteği
    - Fallback mekanizması
    - Rate limiting
    - Cost optimization
    """
    
    def generate_image(self, prompt: str, **kwargs) -> dict:
        """
        AI ile görsel üretir
        
        Args:
            prompt: Görsel açıklaması
            **kwargs: Ek parametreler
            
        Returns:
            dict: Üretilen görsel bilgileri
        """
        # AI provider seçimi
        provider = self.select_best_provider()
        
        # Görsel üretimi
        result = provider.generate(prompt, **kwargs)
        
        # Sonuç işleme
        processed_result = self.process_result(result)
        
        return processed_result
```

### 🔄 Webhook Sistemi

#### Asenkron İşlemler
```python
# Celery task örneği
from celery import shared_task

@shared_task(bind=True)
def generate_ai_image(self, user_id: int, prompt: str, task_id: str):
    """
    Asenkron AI görsel üretimi
    
    - Webhook bildirimleri
    - Progress tracking
    - Error handling
    """
    try:
        # Progress güncelleme
        self.update_state(state='PROGRESS', meta={'progress': 10})
        
        # AI görsel üretimi
        result = ai_service.generate_image(prompt)
        
        # Progress güncelleme
        self.update_state(state='PROGRESS', meta={'progress': 80})
        
        # Sonuç kaydetme
        save_generated_image(user_id, result, task_id)
        
        # Webhook bildirimi
        send_webhook_notification(user_id, task_id, 'completed')
        
        return {'status': 'completed', 'result': result}
        
    except Exception as exc:
        # Hata durumu
        send_webhook_notification(user_id, task_id, 'failed', str(exc))
        raise self.retry(exc=exc, countdown=60, max_retries=3)
```

---

## 🔐 Güvenlik

### 🛡️ Güvenlik Önlemleri

#### JWT Authentication
```python
# JWT ayarları
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}
```

#### CORS Konfigürasyonu
```python
# CORS ayarları
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://mycreatool.com",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

#### Rate Limiting
```python
# Rate limiting
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
        'ai_generation': '10/hour',
    }
}
```

### 🔒 Input Validation

#### Serializer Validation
```python
class AIGenerationSerializer(serializers.Serializer):
    prompt = serializers.CharField(
        max_length=1000,
        help_text="Görsel açıklaması (maksimum 1000 karakter)"
    )
    style = serializers.ChoiceField(
        choices=STYLE_CHOICES,
        default='photorealistic'
    )
    
    def validate_prompt(self, value):
        """Prompt güvenlik kontrolü"""
        # Zararlı içerik kontrolü
        if contains_harmful_content(value):
            raise serializers.ValidationError("Geçersiz içerik")
        
        return value
```

---

## 📊 Veritabanı

### 🗄️ Veritabanı Yapısı

#### CustomUser Modeli
```sql
-- Kullanıcı tablosu
CREATE TABLE accounts_customuser (
    id SERIAL PRIMARY KEY,
    email VARCHAR(254) UNIQUE NOT NULL,
    username VARCHAR(30),
    password VARCHAR(128) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    credits INTEGER DEFAULT 0,
    profile_image VARCHAR(100),
    date_joined TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);
```

#### InviteCode Modeli
```sql
-- Davet kodu tablosu
CREATE TABLE accounts_invitecode (
    id SERIAL PRIMARY KEY,
    code VARCHAR(64) UNIQUE NOT NULL,
    is_used BOOLEAN DEFAULT FALSE,
    used_by_id INTEGER REFERENCES accounts_customuser(id),
    used_at TIMESTAMP,
    used_ip INET,
    used_user_agent TEXT,
    created_by_id INTEGER REFERENCES accounts_customuser(id),
    created_at TIMESTAMP DEFAULT NOW(),
    note VARCHAR(200)
);
```

### 🔄 Migration Yönetimi

#### Migration Komutları
```bash
# Yeni migration oluştur
python manage.py makemigrations

# Migration'ları uygula
python manage.py migrate

# Migration'ları geri al
python manage.py migrate accounts 0001

# Migration durumunu kontrol et
python manage.py showmigrations
```

---

## 🧪 Test

### 🧪 Test Stratejisi

#### Unit Testler
```python
# tests/test_models.py
from django.test import TestCase
from accounts.models import CustomUser, InviteCode

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_creation(self):
        """Kullanıcı oluşturma testi"""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
    
    def test_credit_system(self):
        """Kredi sistemi testi"""
        self.user.credits = 100
        self.user.save()
        self.assertEqual(self.user.credits, 100)
```

#### API Testler
```python
# tests/test_api.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class AccountsAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_registration(self):
        """Kullanıcı kaydı API testi"""
        data = {
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password2': 'newpass123',
            'invite_code': 'valid-invite-code'
        }
        response = self.client.post('/api/accounts/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_login(self):
        """Kullanıcı girişi API testi"""
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post('/api/accounts/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
```

#### Test Çalıştırma
```bash
# Tüm testleri çalıştır
python manage.py test

# Belirli app testleri
python manage.py test accounts

# Coverage raporu
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🚀 Deployment

### 🐳 Docker Production

#### Production Dockerfile
```dockerfile
FROM python:3.10-slim

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodu
COPY . /app
WORKDIR /app

# Production ayarları
ENV DJANGO_SETTINGS_MODULE=mycreatool.settings_production
ENV PYTHONPATH=/app

# Port
EXPOSE 8000

# Gunicorn ile çalıştır
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mycreatool.wsgi:application"]
```

#### Production Settings
```python
# settings_production.py
import os
from .settings import *

# Güvenlik ayarları
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# HTTPS ayarları
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Veritabanı
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Static dosyalar
STATIC_ROOT = '/app/staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media dosyalar
MEDIA_ROOT = '/app/media'
MEDIA_URL = '/media/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/app/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### ☁️ Cloud Deployment

#### Neon PostgreSQL
```bash
# Neon veritabanı bağlantısı
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/neondb?sslmode=require
```

#### Railway/Render Deployment
```yaml
# railway.toml
[build]
builder = "dockerfile"
dockerfilePath = "backend/Dockerfile"

[deploy]
healthcheckPath = "/health/"
healthcheckTimeout = 300
restartPolicyType = "always"
```

---

## 📊 Monitoring & Logging

### 📈 Performance Monitoring

#### Django Debug Toolbar (Development)
```python
# settings.py
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

#### Logging Configuration
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'mycreatool': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

---

## 🔧 Troubleshooting

### 🐛 Yaygın Sorunlar

#### Docker Sorunları
```bash
# Container loglarını kontrol et
docker-compose logs backend

# Container'ı yeniden build et
docker-compose build --no-cache backend

# Port çakışması
netstat -tulpn | grep :8000
```

#### Veritabanı Sorunları
```bash
# Connection test
python manage.py dbshell

# Migration sorunları
python manage.py migrate --fake-initial

# Veritabanı sıfırlama
python manage.py flush
```

#### JWT Token Sorunları
```bash
# Token doğrulama
python manage.py shell
>>> from rest_framework_simplejwt.tokens import AccessToken
>>> token = AccessToken('your-token-here')
>>> print(token.payload)
```

---

## 📞 Destek

**Backend Geliştirici**: Berk Zengin
- **Email**: berkzengin@mycreatool.com
- **GitHub**: [@berkzengin](https://github.com/berkzengin)

**Teknik Destek**:
- **Issues**: GitHub Issues
- **Documentation**: Bu README
- **API Docs**: `/api/docs/` (Swagger UI)

---

<div align="center">

**🚀 Happy Coding!**

Made with ❤️ and Django

</div>