from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy, reverse
from arcana_app.forms import AddTruckForm, AddDriverForm
from arcana_app.models import Driver, Truck, Trailer, Freight, Insurance, Service
from django.views.generic import ListView, TemplateView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


# class AddDriverView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = AddDriverForm()
#         return render(request, 'arcana_app/add_objects.html', {'form': form, 'submit_value_text': 'Add'})
#
#     def post(self, request):
#         form = AddDriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('add_driver'))
#         return render(request, 'arcana_app/add_objects.html', {'form': form, 'submit_value_text': 'Add'})
class AddDriverView(LoginRequiredMixin, CreateView):
    form_class = AddDriverForm
    model = Driver
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_driver')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add driver')
    # def get_form(self, form_class):
    #     form = super(AddDriverView, self).get_form(form_class)
    #     form.fields['birth_date'].widget = forms.DateInput()
    #     return form


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    template_name = 'arcana_app/driver_list.html'


class AddTruckView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddTruckForm()
        return render(request, 'arcana_app/add_objects.html', {'form': form, 'submit_value_text': 'Add'})

    def post(self, request):
        form = AddTruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_truck'))
        return render(request, 'arcana_app/add_objects.html', {'form': form, 'submit_value_text': 'Add'})


class TruckListView(LoginRequiredMixin, ListView):
    model = Truck
    template_name = 'arcana_app/truck_list.html'
