from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email','username','first_name','last_name','age','is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('age',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None,{'fields':('age',)}),
#     )


admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shopcart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PurchaseHistory)