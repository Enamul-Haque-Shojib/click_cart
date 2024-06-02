from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User, CustomerProfile, VendorProfile


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "user_id",
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email"]
    list_filter = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("User Role"),
            {
                 "fields": (
                     "role",
                 )
            },   
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ["email", "username", "first_name", "last_name"]


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "user", "gender", "phone_number"]
    list_filter = ["gender", "phone_number"]
    list_display_links = ["id", "user_id", "user"]


class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "user", "gender", "phone_number"]
    list_filter = ["gender", "phone_number", "company_name"]
    list_display_links = ["id", "user_id", "user"]


admin.site.register(User, UserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(VendorProfile, VendorProfileAdmin)