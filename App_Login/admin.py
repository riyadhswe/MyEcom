from django.contrib import admin
from App_Login.models import User, Profile


# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ['username', 'address_1', 'phone', 'date_joined']


admin.site.register(User)
admin.site.register(Profile,AdminProfile)
