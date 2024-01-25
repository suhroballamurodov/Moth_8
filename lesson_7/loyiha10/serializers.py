from rest_framework import serializers
from .models import Customer, Category, Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

















# # class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
# #     @classmethod
# #     def get_token(cls, user):
# #         token = super().get_token(user)

# #         # Add custom claims
# #         token['username'] = user.username  
# #         token['username'] = user.first_name
# #         token['last_name'] = user.last_name
# #         token['email'] = user.email
# #         return token