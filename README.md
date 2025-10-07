# 🚀 MyCreatool - AI Powered Creative Solutions

<div align="center">

![MyCreatool Logo](https://via.placeholder.com/200x100/4F46E5/FFFFFF?text=MyCreatool)

**Modern AI tabanlı yaratıcı araçlar platformu**

[![Django](https://img.shields.io/badge/Django-5.1.13-green.svg)](https://djangoproject.com/)
[![React](https://img.shields.io/badge/React-19.1.1-blue.svg)](https://reactjs.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue.svg)](https://neon.tech/)

</div>

---

## 📋 İçindekiler

- [🎯 Proje Hakkında](#-proje-hakkında)
- [✨ Özellikler](#-özellikler)
- [🏗️ Teknoloji Stack](#️-teknoloji-stack)
- [🚀 Hızlı Başlangıç](#-hızlı-başlangıç)
- [📁 Proje Yapısı](#-proje-yapısı)
- [🤖 Yapay Zeka Entegrasyonu](#-yapay-zeka-entegrasyonu)
- [🔧 Geliştirme](#-geliştirme)
- [🚀 Deployment](#-deployment)
- [📚 API Dokümantasyonu](#-api-dokümantasyonu)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📄 Lisans](#-lisans)

---

## 🎯 Proje Hakkında

**MyCreatool**, yapay zeka destekli yaratıcı araçlar sunan modern bir web platformudur. Kullanıcılar, AI teknolojisini kullanarak görsel içerik oluşturabilir, düzenleyebilir ve yönetebilirler.

### 🎨 Temel Özellikler
- **AI Görsel Üretimi**: Metin promptlarından yüksek kaliteli görseller oluşturma
- **Görsel Düzenleme**: AI destekli görsel iyileştirme ve manipülasyon
- **Kredi Sistemi**: Adil kullanım için token tabanlı sistem
- **Beta Erişim**: Davet kodu ile kontrollü erişim

---

## ✨ Özellikler

### 🔐 Kullanıcı Yönetimi
- ✅ Email tabanlı kimlik doğrulama
- ✅ JWT token güvenliği
- ✅ Davet kodu sistemi
- ✅ Profil yönetimi
- ✅ Kredi sistemi

### 🎨 AI Görsel İşleme
- ✅ Çok dilli prompt desteği
- ✅ Yüksek kaliteli görsel üretimi
- ✅ Görsel düzenleme araçları
- ✅ Batch işlem desteği

### 🛠️ Geliştirici Dostu
- ✅ RESTful API
- ✅ Docker containerization
- ✅ Real-time işlem takibi
- ✅ Webhook desteği

---

## 🏗️ Teknoloji Stack

### Backend
- **Framework**: Django 5.1.13
- **API**: Django REST Framework
- **Veritabanı**: PostgreSQL (Neon)
- **Kimlik Doğrulama**: JWT
- **Container**: Docker

### Frontend
- **Framework**: React 19.1.1
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Icons**: Heroicons
- **UI Components**: Headless UI

### DevOps & Tools
- **Containerization**: Docker & Docker Compose
- **Database**: Neon PostgreSQL
- **Version Control**: Git
- **Package Manager**: npm, pip

---

## 🚀 Hızlı Başlangıç

### 📋 Gereksinimler

- [Docker](https://docs.docker.com/get-docker/) (v20.10+)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2.0+)
- [Git](https://git-scm.com/downloads)

### ⚡ Kurulum

#### 1. Projeyi Klonlayın
```bash
git clone https://github.com/yourusername/mycreatool.git
cd mycreatool
```

#### 2. Docker ile Çalıştırın
```bash
# Container'ları build edin
docker-compose build

# Servisleri başlatın
docker-compose up -d
```

#### 3. Erişim Adresleri
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin/

#### 4. Admin Giriş Bilgileri
```
Email: nuriakkurt@mycreatool.com
Şifre: Mycreatool123
```

### 🔧 İlk Kurulum Sonrası

#### Veritabanı Migrations
```bash
# Container içinde migrations çalıştırın
docker-compose exec backend python manage.py migrate
```

#### Superuser Oluşturma (Oluşturmaya Gerek Yok, Zaten Var)
```bash
# Yeni admin kullanıcısı oluşturun
docker-compose exec backend python manage.py createsuperuser
```

---

## 📁 Proje Yapısı

```
mycreatool/
├── 📁 backend/                 # Django Backend
│   ├── 📁 accounts/           # Kullanıcı yönetimi
│   ├── 📁 imagegen/           # AI görsel işleme
│   ├── 📁 mycreatool/         # Ana proje ayarları
│   ├── 📄 requirements.txt    # Python bağımlılıkları
│   └── 📄 Dockerfile          # Backend container
├── 📁 frontend/               # React Frontend
│   ├── 📁 src/               # Kaynak kodlar
│   ├── 📄 package.json       # Node.js bağımlılıkları
│   └── 📄 Dockerfile         # Frontend container
├── 📁 profiles/              # Kullanıcı profil resimleri
├── 📄 docker-compose.yml     # Container orkestrasyonu
└── 📄 README.md             # Bu dosya
```

---

## 🤖 Yapay Zeka Entegrasyonu

### 🎯 AI Görsel Üretimi

#### 1. Fotoğraf Üretimi
- **Çok Dilli Destek**: Hangi dilde yazılırsa yazılsın, en doğru sonuçları verir
- **Prompt İyileştirme**: Otomatik prompt optimizasyonu
- **Maliyet Optimizasyonu**: Ekstra maliyet üretmeyecek şekilde tasarlanmış

#### 2. Fotoğraf Düzenleme
- **AI Destekli Düzenleme**: Görsel iyileştirme ve manipülasyon
- **Batch İşlemler**: Toplu görsel işleme
- **Real-time Sonuçlar**: Anlık işlem takibi

### Bu noktadan sonrası ekstra bilgi içindir, fazlasıyla önemi yoktur.
### 🔧 Teknik Implementasyon

#### Backend (imagegen/)
```python
# AI görsel üretimi endpoint'i
POST /api/imagegen/generate/
{
    "prompt": "A beautiful sunset over mountains",
    "language": "en",
    "style": "photorealistic"
}
```

#### Webhook Sistemi
- **Asenkron İşlemler**: Uzun süren AI işlemleri için
- **Real-time Bildirimler**: İşlem durumu takibi
- **Hata Yönetimi**: Güvenilir işlem garantisi

---

## 🔧 Geliştirme

### 🛠️ Geliştirme Ortamı

#### Backend Geliştirme
```bash
# Backend container'ına bağlan
docker-compose exec backend bash

# Django shell
python manage.py shell

# Yeni migration oluştur
python manage.py makemigrations

# Migration'ları uygula
python manage.py migrate

# Testleri çalıştır
python manage.py test
```

#### Frontend Geliştirme
```bash
# Frontend container'ına bağlan
docker-compose exec frontend bash

# Yeni paket ekle
npm install package-name

# Build işlemi
npm run build
```

### 📝 Kod Standartları

#### Python (Backend)
- **PEP 8** standartları
- **Type hints** kullanımı
- **Docstring** dokümantasyonu
- **Türkçe açıklamalar**

#### JavaScript (Frontend)
- **ESLint** konfigürasyonu
- **Prettier** formatlaması
- **Functional components**
- **Hooks** kullanımı

### 🔄 Git Workflow

```bash
# Yeni özellik branch'i oluştur
git checkout -b feature/ai-image-generation

# Değişiklikleri commit et
git add .
git commit -m "feat: AI görsel üretimi özelliği eklendi"

# Branch'i push et
git push origin feature/ai-image-generation

# Pull request oluştur
```

---

## 🚀 Deployment

### 🐳 Docker Production

#### Environment Variables
```bash
# .env dosyası oluşturun
DATABASE_URL=postgresql://user:pass@host:port/db
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

#### Production Build
```bash
# Production build
docker-compose -f docker-compose.prod.yml build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### ☁️ Cloud Deployment

#### Neon PostgreSQL
- **Managed Database**: Otomatik backup ve scaling
- **Global Regions**: Düşük latency
- **Free Tier**: Geliştirme için uygun

#### Vercel/Netlify (Frontend)
- **Static Hosting**: Hızlı CDN dağıtımı
- **Automatic Deploy**: Git push ile otomatik deploy
- **Environment Variables**: Güvenli konfigürasyon

---

## 📚 API Dokümantasyonu

### 🔐 Kimlik Doğrulama

#### Kullanıcı Kaydı
```http
POST /api/accounts/register/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "securepassword",
    "password2": "securepassword",
    "invite_code": "invite-code-uuid"
}
```

#### Giriş
```http
POST /api/accounts/login/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "securepassword"
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
    "style": "photorealistic",
    "quality": "high"
}
```

#### Görsel Düzenleme
```http
POST /api/imagegen/edit/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
    "image": <file>,
    "edit_prompt": "Make it more colorful",
    "operation": "enhance"
}
```

---

## 🧪 Test

### Backend Testleri
```bash
# Tüm testleri çalıştır
docker-compose exec backend python manage.py test

# Belirli app testleri
docker-compose exec backend python manage.py test accounts

# Coverage raporu
docker-compose exec backend coverage run --source='.' manage.py test
docker-compose exec backend coverage report
```

### Frontend Testleri
```bash
# Unit testler
docker-compose exec frontend npm test

# E2E testler
docker-compose exec frontend npm run test:e2e
```

---

## 🐛 Sorun Giderme

### Yaygın Sorunlar

#### Docker Sorunları
```bash
# Container'ları yeniden başlat
docker-compose down
docker-compose up --build -d

# Logları kontrol et
docker-compose logs backend
docker-compose logs frontend
```

#### Veritabanı Sorunları
```bash
# Migration'ları sıfırla
docker-compose exec backend python manage.py migrate --fake-initial

# Veritabanını sıfırla
docker-compose exec backend python manage.py flush
```

#### Port Çakışması
```bash
# Kullanılan portları kontrol et
netstat -tulpn | grep :8000
netstat -tulpn | grep :5173

# Port değiştir (docker-compose.yml)
ports:
  - "8001:8000"  # Backend
  - "5174:5173"  # Frontend
```

---

## 🤝 Katkıda Bulunma

### 📋 Katkı Süreci

1. **Fork** yapın
2. **Feature branch** oluşturun (`git checkout -b feature/amazing-feature`)
3. **Commit** yapın (`git commit -m 'Add amazing feature'`)
4. **Push** edin (`git push origin feature/amazing-feature`)
5. **Pull Request** oluşturun

### 📝 Commit Kuralları

```
feat: Yeni özellik eklendi
fix: Bug düzeltildi
docs: Dokümantasyon güncellendi
style: Kod formatlaması
refactor: Kod yeniden düzenlendi
test: Test eklendi
chore: Build/tool güncellemesi
```

---

## 📊 Proje İstatistikleri

- **Backend**: Django 5.1.13 + PostgreSQL
- **Frontend**: React 19.1.1 + Vite
- **Containerization**: Docker + Docker Compose
- **API**: RESTful + JWT Authentication
- **Database**: Neon PostgreSQL (Cloud)
- **Styling**: Tailwind CSS

---

## 📞 İletişim

**Proje Sahibi**: Berk Zengin
- **Email**: berkzengin@mycreatool.com
- **GitHub**: [@berkzengin](https://github.com/berkzengin)

**Destek**: 
- **Issues**: GitHub Issues kullanın
- **Discussions**: GitHub Discussions
- **Email**: support@mycreatool.com

---

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**

Made with ❤️ by [Berk Zengin](https://github.com/berkzengin)

</div>