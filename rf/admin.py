from django.contrib import admin
from .models import Button, Menu
# Register your models here.

class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0
class MenuAdmin(admin.ModelAdmin):
    list_display = []
    for ff in Menu._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    inlines = [MenuInline,]
    class Meta:
        Model = Menu

admin.site.register(Menu,MenuAdmin )
                                                
class ButtonAdmin(admin.ModelAdmin):
    list_display = []
    for ff in Button._meta.fields:
        list_display.append(ff.name)
    #list_filter = ['type','bu', ]
    #inlines = [MenuInline,]
    class Meta:
        Model = Button

admin.site.register(Button,ButtonAdmin )