from django import forms
from django.core.exceptions import ValidationError
from arcana_app.models import Driver, Truck, Trailer, Insurance


class DateInput(forms.DateInput):
    input_type = 'date'


# class CheckboxInput(forms.CheckboxInput):
#     input_type = 'checkbox'


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AddDriverForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddTruckForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddTruckForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Truck
        fields = '__all__'
        widgets = {
            'begin_MOT': DateInput(),
            'expire_MOT': DateInput(),
        }

        # widgets = {
        #     'has_actual_MOT': forms.CheckboxInput(
        #         attrs={'class': 'required checkbox form-select', 'disabled': 'disabled or true'}),
        # }
