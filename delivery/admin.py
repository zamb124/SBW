from django.contrib import admin
from .models import *
# Register your models here.
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = []
    for ff in DeliveryType._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    #inlines = [DeliveryType,]
    class Meta:
        Model = DeliveryType

admin.site.register(DeliveryType, DeliveryTypeAdmin)

class DeliveryPositionTypeAdmin(admin.ModelAdmin):
    list_display = []
    for ff in DeliveryPositionType._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    #inlines = [DeliveryType,]
    class Meta:
        Model = DeliveryPositionType

admin.site.register(DeliveryPositionType, DeliveryPositionTypeAdmin)

class DeliveryPositionInline(admin.TabularInline):
    model = DeliveryPosition
    extra = 0

class DeliveryPositionAdmin(admin.ModelAdmin):
    list_display = []
    for ff in DeliveryPosition._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    #inlines = [DeliveryPositionInline,]
    class Meta:
        Model = DeliveryPosition
admin.site.register(DeliveryPosition, DeliveryPositionAdmin)

class DeliveryHeadAdmin(admin.ModelAdmin):
    list_display = []
    for ff in DeliveryHead._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    inlines = [DeliveryPositionInline,]
    class Meta:
        Model = DeliveryHead

admin.site.register(DeliveryHead, DeliveryHeadAdmin)

class LogisticDocAdmin(admin.ModelAdmin):
    list_display = []
    for ff in LogisticDoc._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    #inlines = [DeliveryPositionInline,]
    class Meta:
        Model = LogisticDoc

admin.site.register(LogisticDoc, LogisticDocAdmin)



