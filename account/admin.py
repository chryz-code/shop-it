from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(store_staff)
admin.site.register(Store)
admin.site.register(Currency)
# admin.site.register(Shipping_Method)
