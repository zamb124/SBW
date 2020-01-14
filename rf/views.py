from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from .models import Menu
from delivery.models import DeliveryHead
from operations.models import Order

@login_required(login_url='login/')
def menu(request):
    menues = Menu.objects.filter(parent=None)
    return render(request,'rf/menu.html', {'submenues': menues})
# Create your views here.
def main(request):
    url = request.path.split('/')[2]+'/'
    current = Menu.objects.filter(url=url)[0]
    menues = Menu.objects.filter(parent=current.id)
    for i in menues:
        if i.short == 'inbound':
            i.count = DeliveryHead.objects.all().count()#TODO разделить на входящие и исхождящте и подсчитать с фильтром
        if i.short == 'outbound':
            i.count = DeliveryHead.objects.all().count()#TODO разделить на входящие и исхождящте и подсчитать с фильтром
        if i.short == 'internal':
            i.count = Order.objects.filter(status='n' or 'b'or 'p').count()#TODO разделить на входящие и исхождящте и подсчитать с фильтром
    return render(request,'rf/menu.html', {'submenues': menues,'menu': current})
# Create your views here.

