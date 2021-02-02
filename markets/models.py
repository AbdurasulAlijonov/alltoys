from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Mahsulot nomi')
    description = models.TextField(blank=True, null=True, verbose_name='Mahsulot xususiyati')
    price = models.DecimalField(max_digits=20,decimal_places=2,null=True, verbose_name='Narxi')
    addTime = models.DateTimeField(auto_now_add=True,db_index=True, verbose_name='Q\'shilgan vaqti')

    market = models.ForeignKey('Market',on_delete=models.PROTECT, null=True, verbose_name='Do\'kon')

    class Meta:
        verbose_name_plural = 'Mahsulotlar'
        verbose_name = 'Mahsulot'
        ordering = ['addTime']

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Do\'kon')

    class Meta:
        verbose_name_plural = 'Do\'konlar'
        verbose_name = 'Do\'kon'
        ordering = ['name']

    def __str__(self):
        return self.name
