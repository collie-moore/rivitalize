from django.contrib import admin

from apps.promotion.models import Voucher, Package

# Register your models here.
admin.site.register(Voucher)
admin.site.register(Package)