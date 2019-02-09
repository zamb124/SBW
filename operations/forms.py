from django.forms import ModelForm
from django import forms
from .models import  Order, Task
from dal import autocomplete

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {'order_creator': forms.HiddenInput(),'order_updater': forms.HiddenInput() }
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'material':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control','autofocus':'True', 'placeholder':'Введите значение'
            })

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'material':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control','autofocus':'True', 'placeholder':'Введите значение'
        })
    material = forms.ModelChoiceField(
        queryset=Task.objects.all(),
        widget=autocomplete.ModelSelect2(url='material-autocomplete')
    )
    class Meta:
        model = Task
        fields = ('__all__')

class TaskForm2(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')


