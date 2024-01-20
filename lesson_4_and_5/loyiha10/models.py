from django.db import models
# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='Kitob nomi')
    books_author = models.CharField(max_length=50, verbose_name='Muallifi')
    price = models.IntegerField(verbose_name='Narxi')
    user_id = models.IntegerField(verbose_name='User Id')

    def __str__(self):
        return f"{self.title} - {self.books_author}"
    
    class Meta:
        verbose_name = 'Kitob '
        verbose_name_plural = 'Kitoblar '