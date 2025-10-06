from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils import timezone
from .models import InviteCode
import uuid

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "username", "password", "profile_image")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "profile_image", "is_staff", "is_active")}
         ),
    )

@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "note","is_used", "used_by", "used_at", "used_ip", "created_at", "created_by")
    list_filter = ("is_used", "created_at")
    search_fields = ("code", "note", "used_by__email", "used_by__username", "used_ip")
    readonly_fields = ("used_by", "used_at", "used_ip", "used_user_agent", "created_at")
    actions = ["generate_codes", "mark_unused"]

    def generate_codes(self, request, queryset):
        """Admin action: seçili değilken admin arayüzünden toplu kod üret - 1-100 arası isteği sorar."""
        # Bu admin action normalde form isteği gerektirir; burada basit örnek olarak 10 kod üretir:
        created = []
        for _ in range(10):
            c = InviteCode.objects.create(code=str(uuid.uuid4()), created_by=request.user)
            created.append(c.code)
        self.message_user(request, f"10 invite code oluşturuldu. Örnek: {created[:3]}")
    generate_codes.short_description = "Generate 10 invite codes"

    def mark_unused(self, request, queryset):
        updated = queryset.update(is_used=False, used_by=None, used_at=None, used_ip=None, used_user_agent=None)
        self.message_user(request, f"{updated} kod kullanılmamış olarak işaretlendi.")
    mark_unused.short_description = "Mark selected codes as unused"