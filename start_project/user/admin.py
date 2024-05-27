from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# admin.site.register(CustomUser)
# User = get_user_model()

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": ("first_name", "last_name", "email", "country_of_residence", "city_of_residence")
            }),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    inlines = [UserProfileInLine]
    
# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)

