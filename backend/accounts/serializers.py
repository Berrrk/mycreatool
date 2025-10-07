"""
MyCreatool - Kullanıcı Yönetimi Serializer'ları

Bu dosya API veri doğrulama ve dönüştürme işlemlerini içerir.
REST API'de gelen verileri doğrular ve Django model'lerine dönüştürür.

Serializer'lar:
1. RegisterSerializer: Kullanıcı kaydı için veri doğrulama
2. MyTokenObtainPairSerializer: JWT token oluşturma ve doğrulama

Güvenlik Özellikleri:
- Şifre doğrulama
- Davet kodu kontrolü
- IP ve User-Agent takibi
- Input sanitization
"""
from rest_framework import serializers
from .models import CustomUser, InviteCode
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    invite_code = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password2', 'profile_image', 'invite_code')
        extra_kwargs = {'profile_image': {'required': False}}

    def validate(self, attrs):
        """
        Genel veri doğrulama işlemleri
        
        - Şifre eşleşme kontrolü
        - Davet kodu doğrulama
        - Güvenlik kontrolleri
        """
        # Şifre eşleşme kontrolü
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Davet kodu doğrulama
        code = attrs.get('invite_code')
        if not code:
            raise serializers.ValidationError({"invite_code": "Invite code is required."})

        # Kod'un varlığını kontrol et
        try:
            invite_obj = InviteCode.objects.get(code=code)
        except InviteCode.DoesNotExist:
            raise serializers.ValidationError({"invite_code": "Invalid invite code."})

        # Kod'un kullanılmış olup olmadığını kontrol et
        if invite_obj.is_used:
            raise serializers.ValidationError({"invite_code": "This invite code has already been used."})

        return attrs

    def create(self, validated_data):
        """
        Kullanıcı oluşturma işlemi
        
        - Yeni kullanıcı hesabı oluşturur
        - Davet kodunu kullanılmış olarak işaretler
        - IP ve User-Agent bilgilerini kaydeder
        
        Args:
            validated_data: Doğrulanmış kullanıcı verileri
            
        Returns:
            CustomUser: Oluşturulan kullanıcı objesi
        """
        # Gereksiz alanları temizle
        invite_code_value = validated_data.pop('invite_code', None)
        validated_data.pop('password2', None)
        password = validated_data.pop('password')
        # create_user metodu varsa onu kullan:
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # Invite code'u işaretle ve meta bilgiyi kaydet
        if invite_code_value:
            try:
                invite_obj = InviteCode.objects.get(code=invite_code_value, is_used=False)
            except InviteCode.DoesNotExist:
                invite_obj = None

            if invite_obj:
                request = self.context.get('request')
                if request is not None:
                    # IP alma
                    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
                    if x_forwarded_for:
                        ip = x_forwarded_for.split(",")[0].strip()
                    else:
                        ip = request.META.get("REMOTE_ADDR")

                    user_agent = request.META.get("HTTP_USER_AGENT", "")[:1000]

                    invite_obj.is_used = True
                    invite_obj.used_by = user
                    invite_obj.used_at = timezone.now()
                    invite_obj.used_ip = ip
                    invite_obj.used_user_agent = user_agent
                    invite_obj.save()
                else:
                    # context.request yoksa yine işaretle (ip/useragent boş)
                    invite_obj.is_used = True
                    invite_obj.used_by = user
                    invite_obj.used_at = timezone.now()
                    invite_obj.save()

        return user
# Custom token serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # Email ile login yapılacak

    def validate(self, attrs):
        """
        JWT token doğrulama işlemi
        
        - Email ve şifre doğrulaması
        - Token oluşturma
        - Kullanıcı bilgilerini response'a ekleme
        
        Args:
            attrs: Email ve şifre bilgileri
            
        Returns:
            dict: Access token, refresh token ve kullanıcı bilgileri
        """
        # Orijinal JWT doğrulama işlemini çalıştır
        data = super().validate(attrs)
        # Token ile birlikte username de dönsün
        data['username'] = self.user.username
        return data

    @classmethod
    def get_token(cls, user):
        """
        JWT token oluşturma
        
        Token payload'ına kullanıcı bilgilerini ekler.
        
        Args:
            user: Token oluşturulacak kullanıcı
            
        Returns:
            Token: JWT token objesi
        """
        token = super().get_token(user)
        # Token payload içine username ekle
        token['username'] = user.username
        return token
