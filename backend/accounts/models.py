"""
MyCreatool - Kullanıcı Yönetimi Modelleri

Bu dosya kullanıcı kimlik doğrulama ve yetkilendirme sistemini içerir.
Resmi kurum standartlarına uygun güvenlik önlemleri alınmıştır.

Modeller:
1. CustomUserManager: Kullanıcı oluşturma ve yönetimi
2. CustomUser: Özelleştirilmiş kullanıcı modeli (email tabanlı)
3. InviteCode: Davet kodu sistemi (beta erişim kontrolü)

Güvenlik Özellikleri:
- Email tabanlı kimlik doğrulama
- JWT token desteği
- Davet kodu sistemi
- IP ve User-Agent takibi
- Kredi sistemi entegrasyonu
"""
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings


class CustomUserManager(BaseUserManager):
    """
    Özelleştirilmiş Kullanıcı Yöneticisi
    
    Django'nun varsayılan kullanıcı modelini genişletir.
    Email tabanlı kimlik doğrulama sistemi sağlar.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Normal kullanıcı oluşturur
        
        Args:
            email (str): Kullanıcı email adresi (zorunlu)
            password (str): Kullanıcı şifresi
            **extra_fields: Ek kullanıcı bilgileri
            
        Returns:
            CustomUser: Oluşturulan kullanıcı objesi
        """
        if not email:
            raise ValueError('Users must have an email address!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Süper kullanıcı (admin) oluşturur
        
        Args:
            email (str): Admin email adresi
            password (str): Admin şifresi
            **extra_fields: Ek admin bilgileri
            
        Returns:
            CustomUser: Oluşturulan admin kullanıcısı
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)

    profile_image = models.ImageField(upload_to="profiles/", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """Kullanıcının string temsili"""
        return self.email


class InviteCode(models.Model):
    # gösterimi kolay olan uuid string; adminde okunması kolay
    code = models.CharField(max_length=64, unique=True, default=uuid.uuid4)
    is_used = models.BooleanField(default=False)
    used_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="used_invite_codes"
    )
    used_at = models.DateTimeField(null=True, blank=True)
    used_ip = models.GenericIPAddressField(null=True, blank=True)
    used_user_agent = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="created_invite_codes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=200, blank=True, default="")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Invite Code"
        verbose_name_plural = "Invite Codes"

    def __str__(self):
        return str(self.code)