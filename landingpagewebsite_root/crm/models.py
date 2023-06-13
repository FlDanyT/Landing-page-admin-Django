from django.db import models

# Create your models here.
class Order(models.Model):
    #TextField
    name = 'Настройка админки'
    header_name = models.CharField(max_length=200, verbose_name='Верхние название')
    title_description = models.CharField(max_length=200, verbose_name='Заголовок описание')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Изминить информацию на сайте'
        verbose_name_plural = 'Изминить информации на сайте'