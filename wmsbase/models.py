from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, blank=True)
    erpnumber = models.CharField(verbose_name='Номер в ERP', max_length=50, blank=True)
    contact = models.CharField(verbose_name='Контакт', max_length=100, blank=True)
    tel = models.CharField(verbose_name='Телефон', max_length=50, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    adress = models.CharField(verbose_name='Адрес', max_length=50, blank=True)
    def __str__(self):
        return 'Имя: '+self.name

class Material(models.Model): # Материал
    name = models.CharField(verbose_name='Материал', max_length=50, blank=False)
    erpnumber = models.CharField(verbose_name='Номер в ERP', max_length=50, blank=True)
    creator = models.ForeignKey(User, verbose_name="Создал", on_delete=models.SET('Юзер удален'))
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True)
    mtypes = (
        ('M', 'Материал'),
        ('S', 'Услуга'),)
    type = models.CharField(verbose_name='Тип материала',choices=mtypes, max_length=50)
    def __str__(self):
        return str(self.id)+' : '+ self.name

class Uom(models.Model):# Единица измерения
    name = models.CharField(verbose_name='Название ЕИ', max_length=50, blank=False)
    short = models.CharField(verbose_name='Краткое имя', max_length=4, blank=False)
    mtypes = (
        ('M', 'Масса'),
        ('V', 'Обьем'),
        ('T', 'Время'),
        ('E', 'Количественный'),)
    type = models.CharField(verbose_name='Тип ЕИ',choices=mtypes, max_length=50)
    etalon = models.CharField(verbose_name='Является эталоном для', help_text='Устанавливается в случае эталона', choices=mtypes, blank=True, null=True, max_length=100)
    value = models.DecimalField(max_digits=10, verbose_name='Множитель к эталону', help_text='Например, если эталон 1 КГ, в данная единица Г, то будет 0.001, если это эталон, то 1',max_length=10,decimal_places=5)
    def __str__(self):
        return self.short

class BussinesUnit(models.Model):#Номер склада по нашему
    name = models.CharField(verbose_name='Название складского комплекса',help_text='Это ячейка, склад или помещение?', max_length=50, blank=False)
    nameERP = models.CharField(verbose_name='Связь с ERP', max_length=50, blank=False) # Привязывается к логической единице ERP
    def __str__(self):
        return self.name

class WarehouseObjectType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, blank=False)
    short = models.CharField(verbose_name='Краткое имя', max_length=4, blank=False)
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    lowest = models.BooleanField(verbose_name="Инд. низшего уровня", null=True, blank=True, help_text='Устанавливается на низжший уровень в иерархии обьектов например: Ячейка')
    def __str__(self):
        return self.name + ' ' + self.short

class WarehouseObject(models.Model):
    name = models.CharField(verbose_name='Складской обьект',help_text="Помещение\Склад\Область действия\участок склада\ячейка с едиными правилами или свойстави", max_length=50, blank=False)
    parent = models.ForeignKey('self', verbose_name='Вышестоящий обьект', null=True, blank=True, on_delete=models.CASCADE)
    zero = models.BooleanField(verbose_name='Разрешение ОЗ',help_text="Разрещение отрицательного запаса", blank=False)
    short = models.CharField(verbose_name='Краткое имя', max_length=20, blank=False)
    type = models.ForeignKey(WarehouseObjectType, verbose_name='Тип обьекта',on_delete=models.CASCADE)
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    ident = models.CharField(verbose_name='Идентификатор', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class UnitType(models.Model):
    name = models.CharField(verbose_name='Тип юнита', max_length=50, blank=False)
    #short = models.CharField(verbose_name='Краткое имя', max_length=4, blank=False, unique=True)
    def __str__(self):
        return self.name

class Unit(models.Model):
    number = models.CharField(verbose_name='Идентификатор', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Вышестоящий юнит', null=True, blank=True, on_delete=models.CASCADE)
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит', on_delete=models.CASCADE)
    wo = models.ForeignKey(WarehouseObject, verbose_name='Содержится в', blank=False, on_delete=models.CASCADE)
    type = models.ForeignKey(UnitType, verbose_name='Тип юнита', null=True, default=None, blank=False, on_delete=models.SET('Тип юнита удален'))
    def __str__(self):
        return self.number

class Quant(models.Model):
    material = models.ForeignKey(Material, verbose_name="Материал", on_delete=models.SET('Материал удален'))
    wo = models.ForeignKey(WarehouseObject, verbose_name='Содержится в', blank=False,on_delete=models.CASCADE)
    bu = models.ForeignKey(BussinesUnit, verbose_name='Бизнес юнит',on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, verbose_name='Количество', max_length=50, decimal_places=5)
    uom = models.ForeignKey(Uom, verbose_name='Единица измерения',null=True,  on_delete=models.SET('ЕИ Удалена'))
    def __str__(self):
        return str(self.id)
