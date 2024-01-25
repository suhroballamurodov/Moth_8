from rest_framework import generics
from .models import Customer, Category, Product
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import time

class CustomerListAPIView(generics.ListAPIView):
    '''Customerlarni olish uchun'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveAPIView):
    '''Customerlarni id orqali olish uchun'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

class CustomerPurchasesAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        '''Customerning barcha haridlarini id orqali olish uchun'''
        customer_id = self.kwargs['id']
        return Product.objects.filter(user_id=customer_id)



class CustomerPurchasingListAPIView(APIView):
    def get(self, request, customer_id):
        start_time = time(0, 0)  # 00:00
        end_time = time(23, 59)  # 23:00
        purchasing = Product.objects.filter(customer_id=customer_id, create_time__time__range=(start_time, end_time))
        serializer = ProductSerializer(purchasing, many=True)
        return Response({"Haridorning vaqt bo'yicha barcha haridlari haqida ma'lumot":serializer.data})





# def home(request):
#     ''' Application ishlayotganini bilish uchun yozilgan funksiya '''
#     return render(request, 'home.html')


# @api_view(['GET'])
# def get_decode_token(request):
#     ''' Tokenni tekshirish uchun ya'ni faqatgina admin yoki user CRUD amallarini bajara olish uchun yozilgan funksiya '''
#     decode_token = jwt.decode(request.META['HTTP_TOKEN'])
#     return Response({'token': decode_token})
   

# class CategoryModelViewset(ModelViewSet):
#     ''' CRUD amallarni bajarish uchun '''
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# # class CustomerModelViewset(ModelViewSet):
# #     queryset = Customer.objects.all()
# #     serializer_class = ProductSerializer


# class ProductModelViewset(ModelViewSet):
#     ''' CRUD amallarni bajarish uchun '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class PurchaseModelViewset(ModelViewSet):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
#     # def get(self, request, customer_id):
#     #     '''Customerni barcha haridlarini olish uchun'''
#     #     purchases = Purchase.objects.filter(customer_id=customer_id)
#     #     serializer = PurchaseSerializer(purchases, many=True)
#     #     return Response(serializer.data)
    
# # class CustomerViewSet(viewsets.ModelViewSet):
# #     queryset = Customer.objects.all()
# #     serializer_class = CustomerSerializer

# # class ProductViewSet(viewsets.ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer