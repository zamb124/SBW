from django.db import models
from wmsbase.models import BussinesUnit, Material,Uom, WarehouseObject, Client
from django.contrib.auth.models import User
from wmsbase.models import Quant, Unit, Uom

class Order(models.Model):
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Клиент', default=None, null=True, blank=True, on_delete=models.SET(None))
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    order_creator = models.ForeignKey(User, related_name= 'creator', verbose_name="Создал", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при создании
    order_updater = models.ForeignKey(User,  related_name= 'updater', verbose_name="Изменил", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при изменении
    status = (('b', 'Пустой'),
              ('n', 'Новый'),
              ('p', 'Выполняется'),
              ('d', 'Завершен'),
              )
    status = models.CharField(verbose_name='Статус', max_length=20, choices=status, blank=True, default='Пустой')

    def __str__(self):
        return str(self.id)

class Task(models.Model):
    order = models.ForeignKey(Order, verbose_name='Складской заказ', null=True, on_delete=models.CASCADE)
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, verbose_name="Материал", on_delete=models.SET('Материал удален'))
    uom = models.ForeignKey(Uom, verbose_name='Единица измерения', null=True, on_delete=models.SET('ЕИ Удалена')) #TODO Единица перемещения, не зависит от кванта, целевое для перемещения
    value = models.DecimalField(max_digits=10, verbose_name='Количество', max_length=50, decimal_places=5)  #Количество перемещаемое
    source = models.ForeignKey(WarehouseObject, related_name= 'bin_out',verbose_name='Источник', default=None, null=False, blank=False, on_delete=models.SET(None))
    dest = models.ForeignKey(WarehouseObject, related_name= 'bin_inn', verbose_name='Назначение', default=None, null=False, blank=False, on_delete=models.SET(None))
    creator = models.ForeignKey(User, related_name= 'create',verbose_name="Создал", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при создании
    updater = models.ForeignKey(User, related_name= 'update',verbose_name="Изменил", on_delete=models.SET('Юзер удален'))#TODO: Добавить сценарий при изменении
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    quant = models.ForeignKey(Quant, verbose_name='Квант', null=True, blank=True, on_delete=models.CASCADE)# TODO Если тащится не квант целиком, то создать новый квант и записать сюда его!
    unit = models.ForeignKey(Unit, verbose_name='Квант', null=True, blank=True,on_delete=models.CASCADE) # упаковка
    status = (('b', 'Пустой'),
              ('n', 'Новый'),
              ('p', 'Выполняется'),
              ('d', 'Завершен'),
              )
    status = models.CharField(verbose_name='Статус', max_length=20, choices=status, blank=True, default='Пустой')

    def __str__(self):
        return str(self.id)

class OrderSettings(models.Model):
    name = models.CharField(verbose_name='Название настройки', blank=True, max_length=100, null=True)
    imgorder = models.ImageField(verbose_name='Image')

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(verbose_name='Название маршрута', blank=True, max_length=100, null=True)
    def __str__(self):
        return self.name
