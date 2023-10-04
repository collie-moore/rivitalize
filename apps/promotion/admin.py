from django.contrib import admin

from apps.promotion.models import Voucher, Package

# Register your models here.
admin.site.index_title = "Welcome to Revitalize Portal"
admin.site.site_header = "Revitalize Admin"
admin.site.site_title = " Revitalizen Admin Portal"
admin.site.register(Voucher)
admin.site.register(Package)