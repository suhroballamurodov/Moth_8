from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user_id = models.IntegerField()


    def __str__(self):
        return self.name




















# # class Category(models.Model):
# #     name = models.CharField(max_length=50,verbose_name='Kategory')

# #     def __str__(self):
# #         return self.name


# # class Customer(models.Model):
# #     name = models.CharField(max_length=30, verbose_name='Ism')
# #     l_name = models.CharField(max_length=30, verbose_name='Familiyasi')
# #     age = models.IntegerField(verbose_name='Yoshi')

# #     def __str__(self):
# #         return self.name


# # class Product(models.Model):
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
# #     name = models.CharField(max_length=50, verbose_name='Maxsulot nomi')
# #     prise = models.IntegerField(verbose_name='Narxi')
# #     total = models.IntegerField(verbose_name='Soni')
    
# #     def __str__(self):
# #         return self.name


# # class Category(models.Model):
# #     name = models.CharField(max_length=200)

# # class Customer(models.Model):
# #     name = models.CharField(max_length=200)

# # class Product(models.Model):
# #     name = models.CharField(max_length=200)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     customers = models.ManyToManyField(Customer, through='Purchase')

# # class Purchase(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# #     purchase_date = models.DateTimeField(auto_now_add=True)








# # class Books(models.Model):
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=50, verbose_name='Kitob nomi')
# #     books_author = models.CharField(max_length=50, verbose_name='Muallifi')
# #     price = models.IntegerField(verbose_name='Narxi')
# #     user_id = models.IntegerField(verbose_name='User Id')

# #     def __str__(self):
# #         return f"{self.title} - {self.books_author}"
    
# #     class Meta:
# #         verbose_name = 'Kitob '
# #         verbose_name_plural = 'Kitoblar '