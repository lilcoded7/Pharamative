from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()

admin.site.site_header = 'CAF-FOOD'
admin.site.site_title = 'CAF-FOOD'

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(User, UserAdmin)