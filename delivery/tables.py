from django.forms import ModelForm
from .models import  DeliveryHead, DeliveryPosition
import django_tables2 as tables
from django.utils.html import format_html

class MyColumn(tables.Column):
    def velue(self, value):
        return str(value)+'1'

class DeliveryTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', orderable=False)
    открыть = tables.TemplateColumn('<a class="btn-sm btn-primary" href="/delivery/{{ record.id }}" role="button">Открыть</a>')
    #positions = tables.Column(orderable=False)
    values = tables.TemplateColumn('<a href= #> <span class="badge bg-primary">{{ record.positions }}</span> </a>', template_name='Колво', accessor='Кол=во')

    class Meta:
        model = DeliveryHead
        exclude  = ('positions','date_update','updater',)
        sequence = ('id','selection','открыть',  '...',)
        template_name = 'django_tables2/bootstrap.html'


class DeliveryPosTable(tables.Table):
    #count =  DeliveryPosition.objects.filter(pk=кусщкв)
    selection = tables.CheckBoxColumn(accessor='pk', orderable=False)
    открыть = tables.TemplateColumn('<a class="btn btn-primary" href="/delivery/{{ record.id }}" role="button">Посмотреть\изменить</a>')
    values=tables.TemplateColumn('<a href= #> <span class="badge bg-primary">5</span> </a>', template_name='Колво')
    #positions = tables.TemplateColumn('<a href= #> <span class="badge bg-primary">5</span> </a>', template_name='Колво')
    
    class Meta:
        model = DeliveryPosition
        sequence = ('id','selection','открыть',  '...',)
        template_name = 'django_tables2/bootstrap.html'
        exclude_columns =('positions',)
        row_attrs = {
            'data-id': lambda record: record.pk,
            'name': lambda record: record.pk,
        }






