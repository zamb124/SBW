from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm,TaskForm2, OrderForm
from .models import Material,Order
from dal import autocomplete
from django.forms import inlineformset_factory
from .tables import OrdersTable
from django_tables2 import RequestConfig
from operations.operations import create_order

@login_required(login_url='login/')
def operations(request):#Вывести все задачи? TODO: Переделать на вывод и поставок тоже
    querry = Task.objects.all().order_by('-id')[:100]
    infopanel = {}
    infopanel['operations'] = operations = Task.objects.all().count()
    
    return render(request,'operations.html',{'object_list': querry, 'infopanel':infopanel, 'path': request.path} )

@login_required(login_url='login/')
def order_create(request): # структура склада запас
    OrderFormSet = inlineformset_factory(Order, Task, form=TaskForm)
    task = {}
    if request.method == 'POST':
        user = request.user.id
        order = create_order(user, request.POST)
        if not order.get('error'):
            return render(request, 'orderSex.html', {'order': order.get('order'), 'tasks': order.get('tasks')})
        else:
            return render(request, 'orderSex.html', {'error': order.get('error'),})
    else:
        form = OrderForm()
        task= OrderFormSet()
    return render(request,'order.html',{'form':form ,'TaskSet': task} )

@login_required(login_url='login/')
def orders(request):
    table = OrdersTable(Order.objects.all())
    pks = request.POST.getlist("selection")
    if request.method == "POST":
        selected_objects = Order.objects.filter(pk__in=pks) #Выбрать обьекты
    RequestConfig(request).configure(table)   # вообще не знаю зачем так)
    table.paginate(page=request.GET.get('page', 1), per_page=25)  #Вставляем пегинацию
    return render(request, 'orders.html', {'table': table})



class MaterialAutocomplete(autocomplete.Select2QuerySetView): # Класс для автозаполнения
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Material.objects.none()
        qs = Material.objects.all()
        sq = qs
        if self.q:
            qs = qs.filter(name__istartswith=self.q) # Поиск по имени
        if not qs:
            qs = sq.filter(id__istartswith=self.q) # Если не найдено, поиск по ID
        return qs