from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryHead, DeliveryType, DeliveryPosition
from .tables import DeliveryTable
from django_tables2 import RequestConfig
from operations.models import Task
# Create your views here.
@login_required(login_url='login/')
def deliveries(request):
    objects = DeliveryHead.objects.all()
    heads = []
    for o in objects:
        o.positions = DeliveryPosition.objects.filter(delivery = o.id).count()
        heads.append(o)
    table = DeliveryTable(heads)
    pks = request.POST.getlist("selection")
    if request.method == "POST":
        selected_objects = DeliveryHead.objects.filter(pk__in=pks)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=25)
    infopanel = {}
    infopanel['operations'] = Task.objects.all().count()
    return render(request, 'deliveries.html', {'table': table, 'infopanel':infopanel})

def delivery(request):#Вывести все задачи? TODO: Переделать на вывод и поставок тоже
    querry = DeliveryHead.objects.all().order_by('-id')[:100]
    infopanel = {}
    infopanel['operations'] = operations = DeliveryHead.objects.all().count()
    return render(request,'deliveries.html',{'object_list': querry, 'infopanel':infopanel, 'path': request.path} )