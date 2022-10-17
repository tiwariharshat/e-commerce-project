from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem, Profile


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItem)