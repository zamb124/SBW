from django.forms import ModelForm
from .models import DeliveryHead, DeliveryPosition


class DeliveryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        delivery_type = kwargs.pop('delivery_type', [])
        super(DeliveryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        self.fields['delivery_type'].queryset = delivery_type

    class Meta:
        model = DeliveryHead
        fields = (
            'delivery_type', 'number', 'partner', 'creator', 'updater', 'date_create', 'date_update', 'positions'
        )

class DeliveryPositionForm(ModelForm):
    class Meta:
        model = DeliveryPosition
        fields = ('__all__')



