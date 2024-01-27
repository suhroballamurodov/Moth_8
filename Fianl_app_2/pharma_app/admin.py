from django.contrib import admin
from .models import *



#concact page uchun
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','email','subject', 'message')
    search_fields = ['name','last_name','email']
    ordering = ['name','last_name']



#dorilar uchun
class PharmaAdmin(admin.ModelAdmin):
    list_display = ('pharma_name', 'pharma_about','pharma_price')
    search_fields = ['pharma_name','pharma_price']
    ordering = ['pharma_name','pharma_price']



#yetkazib berish uchun
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'city', 'company_name', 'phone')
    search_fields = ['name', 'region', 'city', 'company_name', 'phone']
    ordering = ['region', 'city', 'company_name']



admin.site.register(UserModel, UserAdmin)
admin.site.register(PharmaModel,PharmaAdmin)
admin.site.register(DeliveryModel, DeliveryAdmin)