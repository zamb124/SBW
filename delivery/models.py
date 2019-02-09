from django.db import models
from django.contrib.auth.models import User
from wmsbase.models import BussinesUnit, Material,Uom, WarehouseObject, Client
# Create your models here.
class DeliveryType(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, help_text='Типа поставок может меняться от применения',  blank=False)
    short = models.CharField(verbose_name='Короткое имя', max_length=5, help_text='Краткое имя',unique=True, blank=False, null=False)
    types = (('inn', 'Входящая'),
              ('out', 'Исходящая'),
              ('int', 'Внутренняя'),
              )
    status = models.CharField(verbose_name='Направление', max_length=20, choices=types, default='Входящая')
    erp_link = models.CharField(verbose_name='Тип поставки ERP', max_length=40, help_text='Ссылка на тип поставки в ERP истемах, можно использовать как имя сервиса', blank=True, null=True)
    def __str__(self):
        return self.name

class DeliveryPositionType(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, help_text='Типа поставок может меняться от применения',  blank=False)
    short = models.CharField(verbose_name='Короткое имя', max_length=5, help_text='Краткое имя',unique=True, blank=False, null=False)
    erp_link = models.CharField(verbose_name='Тип позиции поставки ERP', max_length=40, help_text='Ссылка на тип позиции поставки в ERP истемах, можно использовать как имя сервиса', blank=True, null=True)
    def __str__(self):
        return self.name


class DeliveryHead(models.Model):
    delivery_type = models.ForeignKey(DeliveryType, null=True, verbose_name='Тип поставки', blank=True, on_delete=models.SET('Тип удален'))
    number = models.CharField(verbose_name='Номер поставки ERP', max_length=100, help_text='Номер поставки из внешней системы',  blank=True)
    partner = models.CharField(verbose_name='Партнер', max_length=100,  blank=True)
    creator = models.ForeignKey(User, related_name= 'createHead',verbose_name="Создал", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при создании
    updater = models.ForeignKey(User, related_name= 'updateHead',verbose_name="Изменил", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при изменении
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Дата Изменения", auto_now=True)
    positions = models.IntegerField(verbose_name="Количество позиций", default=0, null=True, blank=False,)
    def __str__(self):
        return self.number

class DeliveryPosition(models.Model):
    delivery_position_type = models.ForeignKey(DeliveryPositionType, verbose_name='Тип позиции поставки', null=True, blank=True, on_delete=models.CASCADE)
    delivery = models.ForeignKey(DeliveryHead, verbose_name='Поставка', on_delete=models.CASCADE)
    pos_number = models.IntegerField(verbose_name='Номер позиции в поставке', blank=False) # TODO: сценарий создания и распределение номеров позиций
    material = models.ForeignKey(Material, verbose_name="Материал", on_delete=models.SET('Материал удален'))
    value = models.DecimalField(max_digits=10, verbose_name='Количество', max_length=50, decimal_places=5)
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    creator = models.ForeignKey(User, related_name='createDeliveryPos',verbose_name="Создал", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при создании
    updater = models.ForeignKey(User, related_name='updateDeliveryPos',verbose_name="Изменил", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при изменении
    def __str__(self):
        return str(self.pos_number) + str(self.material)

class LogisticDoc(models.Model):
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    partner = models.ForeignKey(Client, verbose_name='Партнер', on_delete=models.CASCADE)
    delivery = models.ForeignKey(DeliveryHead, verbose_name='Документ основание',null=False, blank=True, on_delete=models.SET('Поставка удалена'))
    delivery_pos = models.ForeignKey(DeliveryPosition, verbose_name='Документ основание', null=False, blank=True,on_delete=models.SET('Поставка удалена') )
    value = models.DecimalField(max_digits=10, verbose_name='Количество', max_length=50, decimal_places=5)
    uom = models.ForeignKey(Uom, verbose_name='Единица измерения', null=True, on_delete=models.SET('ЕИ Удалена'))  # TODO Единица перемещения, не зависит от кванта, целевое для перемещения
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    creator = models.ForeignKey(User, related_name='creatorLogDoc',verbose_name="Создал", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при создании
    updater = models.ForeignKey(User, related_name='updaterLogDoc',verbose_name="Изменил", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при изменении
    def __str__(self):
        return self.delivery