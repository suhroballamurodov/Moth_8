from django.db import models




#contact page uchun 
class UserModel(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Ismi')
    last_name = models.CharField(max_length=40, blank=False, verbose_name='Familiyasi')
    email = models.EmailField(blank=False, verbose_name='Email')
    subject = models.TextField(blank=True, verbose_name='Qisqacha')
    message = models.TextField(blank=True, verbose_name='Xabar')

    def __str__(self):
        return self.name, self.last_name
    
    class Meta:
        verbose_name = "Kontakt ma'lumoti"
        verbose_name_plural = "Kontakt ma'lumotlari"




#dorilarni bazaga qo'shish uchun
class PharmaModel(models.Model):
    pharma_name = models.CharField(max_length=50,blank=False, verbose_name='Dori nomi')
    pharma_about = models.TextField(blank=True, verbose_name='Dori haqida')
    pharma_price = models.IntegerField(blank=False, verbose_name='Narhi')
    image = models.ImageField(null=True, blank=True,verbose_name='Rasmi') #pillow install next working
 
    def __str__(self):
        return self.pharma_name
    
    class Meta:
        verbose_name = 'Dori'
        verbose_name_plural = 'Dorilar'



#belling details
#yetkazib berish uchun 
class DeliveryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Ismi')
    last_name = models.CharField(max_length=40, blank=False, verbose_name='Familiyasi')
    region = models.CharField(max_length=20, blank=False, verbose_name='Viloyat')
    city = models.CharField(max_length=30, blank=False, verbose_name='Shahar')
    company_name = models.CharField(max_length=40, blank=False, verbose_name='Dorixona nomi')
    address = models.TextField(blank=False, verbose_name='Manzil')
    posta_code = models.IntegerField(blank=False, verbose_name='Pochta kodi')
    email = models.EmailField(blank=False, verbose_name='Email')
    phone = models.IntegerField(blank=False,verbose_name='Telefon nomer')
    message = models.TextField(blank=True, verbose_name='Xabar')

    def __str__(self):
        return self.name, self.region, self.company_name
    
    class Meta:
        verbose_name = 'Buyurtma '
        verbose_name_plural = 'Buyurtmalar '

