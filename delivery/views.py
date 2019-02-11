from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryHead, DeliveryType, DeliveryPosition
from .tables import DeliveryTable
from django_tables2 import RequestConfig
from operations.models import Task
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View)
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

@login_required(login_url='login/')
def delivery(request, id):#Вывести все задачи? TODO: Переделать на вывод и поставок тоже
    return render(request,'delivery.html',{})

class DeliveryView(DetailView):
    model = DeliveryHead
    context_object_name = "delivery"
    template_name = "delivery.html"
    def get_queryset(self):
        queryset = super(DeliveryView, self).get_queryset()
        return queryset.select_related("delivery_type")

    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        context.update({"positions": context["delivery"].delivery_position.all(),})
        return context