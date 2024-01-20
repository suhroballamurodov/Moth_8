from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BooksModelViewset, basename='books') #api/books orqali API ma'lumotlarni ko'rish mumkin

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #tokenni olish
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #agar token eskirsa refresh berib yangilash uchun
] + router.urls
 