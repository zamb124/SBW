from django.contrib import admin
from .models import *







class TaskAdmin(admin.ModelAdmin):
    list_display = []
    for ff in Task._meta.fields:
        list_display.append(ff.name)
    list_filter = ['order','creator', ]
    class Meta:
        Model = Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    list_display = []
    for ff in Order._meta.fields:
        list_display.append(ff.name)
    list_filter = ['order_creator','client', ]
    inlines = [TaskInline]
    class Meta:
        Model = Order

admin.site.register(Order,OrderAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(OrderSettings)
# Register your models here.
