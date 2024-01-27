from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from datetime import time
from rest_framework import generics
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from django.views import View
# import pandas as pd
import openpyxl


def final(request):
    return HttpResponse('My Final applications view')

class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomerAPIView(viewsets.ModelViewSet):
    '''Customerlarni olish uchun'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductAPIView(viewsets.ModelViewSet):
    '''Customerlarni id orqali olish uchun'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def export_haridlar_to_excel(*args, **kwargs):
    '''Excelga malumotlarni yozish uchun'''
    haridlar = Product.objects.all()
    serializer = ProductSerializer(haridlar, many=True)
    data = serializer.data

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_num, row_data in enumerate(data, start=1):
        for col_num, value in enumerate(row_data.values(), start=1):
            sheet.cell(row=row_num, column=col_num, value=value)

    workbook.save('haridlar.xlsx')



class ShopcardApiView(viewsets.ModelViewSet):
    queryset = Shopcart.objects.all()
    serializer_class = ShopcardSerializer


class OrderApiViews(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemApiViews(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class TimeListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        start_time = time(11, 0)  # 00:00
        end_time = time(19, 20)  # 23:00
        return Product.objects.filter(create_time__time__range=(start_time, end_time))
 

class CustomerPurchasing(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self, request, *args, **kwargs):
        data = list(Product.objects.filter(id=kwargs['pk']).values())
        return Response(data)
    

class CustomerPurchaseSummaryView(viewsets.ModelViewSet):
    '''Customerni barcha haridlari 1 mln dan ytuqori ekanligini tekshiruvchi API'''
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    def retrieve(self, request, *args, **kwargs):

        customer = get_object_or_404(Customer, id=kwargs['pk'])
        purchases = PurchaseHistory.objects.filter(customer=customer)

        total_quantity = sum(purchase.quantity for purchase in purchases)
        total_amount = sum(purchase.total_price for purchase in purchases)
        # response_data = {
        #     "Mijoz ismi": customer.f_name,
        #     "Haridlar soni": total_quantity,
        #     "Umumiy narx": total_amount
        # }
        return Response({'Umumiy summa':total_amount,'Aksiya ishtirokchisimi': total_amount > 1000000})



class ProductAPIView(viewsets.ModelViewSet):
    '''Umumiy maxsulotlar summasini olib keluvchi API'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self, request, *args, **kwargs):
        purchases = Product.objects.all()
        total_amount = sum(purchase.price for purchase in purchases)
        return Response({'Umumiy maxsulotlar summasi':total_amount})