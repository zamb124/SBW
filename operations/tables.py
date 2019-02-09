from django.forms import ModelForm
from .models import  Order, Task


import django_tables2 as tables

class OrdersTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', orderable=False)
    открыть = tables.TemplateColumn('<a class="btn-sm btn-primary" href="/operations/orders/{{ record.id }}" role="button">Открыть</a>')
    values=tables.TemplateColumn('<a href= #> <span class="badge bg-primary">5</span> </a>', template_name='Колво')

    class Meta:
        model = Order
        sequence = ('id','selection','открыть',  '...',)
        template_name = 'django_tables2/bootstrap.html'
        row_attrs = {
            'data-id': lambda record: record.pk,
            'name': lambda record: record.pk,
        }






