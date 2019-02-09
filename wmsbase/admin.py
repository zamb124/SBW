from django.contrib import admin
from .models import *
admin.site.register(Client)

class WarehouseObjectInline(admin.TabularInline):
    model = WarehouseObject
    extra = 0

class Client(admin.ModelAdmin):
    list_display = []
    for ff in Client._meta.fields:
        list_display.append(ff.name)
    class Meta:
        Model = Client

class WarehouseObjectAdmin(admin.ModelAdmin):
    list_display = []
    for ff in WarehouseObject._meta.fields:
        list_display.append(ff.name)
    list_filter = ['type','bu', ]
    inlines = [WarehouseObjectInline,]
    class Meta:
        Model = WarehouseObject


admin.site.register(WarehouseObject,WarehouseObjectAdmin )


admin.site.register(Material)
admin.site.register(Uom)
admin.site.register(BussinesUnit)
admin.site.register(WarehouseObjectType)
admin.site.register(UnitType)
admin.site.register(Unit)
admin.site.register(Quant)

# Register your models here.
