from django.contrib import admin
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInLine]
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

