from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import CustomerListAPIView, CustomerDetailAPIView, CustomerPurchasesAPIView

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('docs/', schema_view),
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'), #Customerlarni olish uchun API
    path('customers/<int:id>/', CustomerDetailAPIView.as_view(), name='customer-detail'), #Customerlarni id olish uchun API
    path('customers/<int:id>/purchases/', CustomerPurchasesAPIView.as_view(), name='customer-purchases'), #Customerlarning barcha hariqlarini id orqali olish uchun API
]
