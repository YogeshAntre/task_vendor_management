# from django.contrib import admin

# # Register your models here.
# # admin.py

# from django.contrib import admin
# from .models import Vendor, PurchaseOrder, HistoricalPerformance

# @admin.register(Vendor)
# class VendorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'contact_details', 'vendor_code', 'on_time_delivery_rate')

# @admin.register(PurchaseOrder)
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     list_display = ('po_number', 'vendor', 'order_date', 'status')

# @admin.register(HistoricalPerformance)
# class HistoricalPerformanceAdmin(admin.ModelAdmin):
#     list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg')
# admin.py

from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)
