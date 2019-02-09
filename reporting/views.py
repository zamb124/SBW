from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from wmsbase.models import WarehouseObject, Quant
from operations.models import *
from django.conf import settings
# Create your views here.

@login_required(login_url='login/')
def structure(request):
    lgorts_all = WarehouseObject.objects.all()
    lgorts = []
    lowers = []
    for l in lgorts_all:
        if l.type.lowest != True and l.parent == None:
            lgorts.append(l)
        for low in lgorts_all:
            if low.parent_id == l.id and low.type.lowest != True:
                lowers.append(low)

    path = line(request)#Заполнение для навигационной панели
    infopanel = {}
    infopanel['operations'] = operations = Task.objects.all().count()
    return render(request,'structure.html', {'infopanel': infopanel,'lgorts': lgorts, 'lowers': lowers, 'path': path[0], 'last': path[1]   })


@login_required(login_url='login/')
def warehouses(request, id): # структура склада запас
    lgort = WarehouseObject.objects.filter(id=id)
    all = []
    locations = []
    bins = []
    quants = []
    locations_qerry = WarehouseObject.objects.filter(parent_id=id)
    for s in locations_qerry:
        all.append(s)
    for s2 in lgort:
        all.append(s2)
    for i in all:
        if i.type.lowest != True:
            locations.append(i)
            querry_bins = WarehouseObject.objects.filter(parent_id=i.id)
            for b in querry_bins:
                if b.type.lowest == True:
                    bins.append(b)
    if not locations: #Значит это ячейка
        for v in lgort:
            locations.append(v)
            querry_quants = Quant.objects.filter(wo_id=v.id)
            for t in querry_quants:
                quants.append(t)
    path = line(request)  # Заполнение для навигационной панели
    infopanel = {}
    infopanel['operations'] = operations = Task.objects.all().count()
    return render(request,'warehouses.html', {'infopanel': infopanel, 'lgorts':locations, 'lowers': bins,'quants': quants, 'path': path[0], 'last': path[1]})

def line(request): #Заполнение для навигационной панели
    url = request.path.split('/')[1:-1]
    path = []
    d = ''
    for str in url:
        path.append({'name':str.title(), 'url': d+str})
        d = d+str+'/'
    last = path[-1].get('name')
    return [path, last]