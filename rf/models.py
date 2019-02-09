from django.db import models

class Menu(models.Model):
    name = models.CharField(verbose_name='Меню',help_text="Меню", max_length=50, blank=False)
    parent = models.ForeignKey('self', verbose_name='Вышестоящее меню', null=True, blank=True, on_delete=models.CASCADE)
    conteiner = models.BooleanField(verbose_name='Является контейнером',help_text="если активно, то меню является контейнером для других меню", blank=False)
    short = models.CharField(verbose_name='Краткое имя', max_length=20, blank=False)
    url = models.CharField(verbose_name='URL Меню или метода', max_length=100, blank=True, null=True)
    count = models.CharField(verbose_name='Количество операций', default='0',max_length=100, blank=True, null=True)
    keyid = models.CharField(verbose_name='id Кнопки', default='0', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Button(models.Model):
    name = models.CharField(verbose_name='Название кнопки', max_length=50, blank=False)
    short = models.CharField(verbose_name='Кнопка',help_text="Нужно вписать кнопку по стандарту", max_length=20, blank=False) #TODO Нужно сделать js библиотеку, для реагирования на кнопки, назад, вперед, стереть, и тд
    def __str__(self):
        return self.name
