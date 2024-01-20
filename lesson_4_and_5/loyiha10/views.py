from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
import jwt
from rest_framework.viewsets import ModelViewSet



@api_view(['GET'])
def get_decode_token(request):
    ''' Tokenni tekshirish uchun ya'ni faqatgina admin yoki user CRUD amallarini bajara olish uchun yozilgan funksiya '''
    decode_token = jwt.decode(request.META['HTTP_TOKEN'])
    return Response({'token': decode_token})


class BooksModelViewset(ModelViewSet):
    ''' CRUD amallarni bajarish uchun '''
    queryset = Books.objects.all()
    serializer_class = BookSerializer


def home(request):
    ''' Application ishlayotganini bilish uchun yozilgan funksiya '''
    return render(request, 'home.html')