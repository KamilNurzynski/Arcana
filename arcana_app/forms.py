from django import forms
from django.core.exceptions import ValidationError
from arcana_app.models import Driver, Truck, Trailer, Insurance, Freight


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


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


class AddTrailerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddTrailerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Trailer
        fields = '__all__'
        widgets = {
            'begin_MOT': DateInput(),
            'expire_MOT': DateInput(),
        }


class AddInsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddInsuranceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Insurance
        fields = '__all__'

    def clean(self):
        data = super().clean()
        if not data['begin_date'] <= data['end_date']:
            raise ValidationError("Begin date can't be earlier than end date!")
        return data


class AddFreightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddFreightForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Freight
        fields = '__all__'
        widgets = {
            'date_of_loading': DateInput(),
            'date_of_unloading': DateInput(),
            'hour_of_loading': TimeInput(),
            'hour_of_unloading': TimeInput(),
        }
