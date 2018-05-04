from django.contrib import admin
from store.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    exclude = ('updated_at',)

admin.site.register(Order, OrderAdmin)