from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *


# Unregister your models here.
admin.site.unregister(Group)



class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)