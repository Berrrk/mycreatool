"""
MyCreatool - Accounts Uygulaması Yapılandırması

Bu dosya accounts Django uygulamasının yapılandırma ayarlarını içerir.
Kullanıcı yönetimi modülünün Django projesine entegrasyonunu sağlar.
"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Accounts Uygulaması Yapılandırması
    
    Kullanıcı yönetimi modülünün Django projesindeki yapılandırması.
    Custom user model ve kimlik doğrulama sistemi için gerekli ayarlar.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
