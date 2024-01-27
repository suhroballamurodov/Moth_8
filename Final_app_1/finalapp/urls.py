from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryApiView, basename='category') #api/books orqali API ma'lumotlarni ko'rish mumkin
router.register(r'customer', CustomerAPIView, basename='customer')
router.register(r'product', ProductAPIView, basename='product')
router.register(r'shopcard', ShopcardApiView, basename='shopcard')
router.register(r'order', OrderApiViews, basename='order')
router.register(r'orderitem', OrderItemApiViews, basename='orderitems')
router.register(r'time', CustomerPurchasing, basename='time')
router.register(r'total',CustomerPurchaseSummaryView, basename='total')
router.register(r'total_product',ProductAPIView, basename='total_product')




urlpatterns = [
    path('', final, name='final'),
    path('product/<int:med_id>/time',TimeListAPIView.as_view()),
    path('exsel/', export_haridlar_to_excel, name='exsel'),
    # path('customer/<int:customer_id>/purchases', CustomerPurchaseSummaryView.as_view(), name='customer_purchase_summary'),
    # path('customers/<int:customer_id>/product', CustomerPurchasing.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #tokenni olish
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #agar token eskirsa refresh berib yangilash uchun
] + router.urls