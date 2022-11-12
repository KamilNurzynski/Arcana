from django.shortcuts import render, redirect
from django import forms
import datetime
from django.urls import reverse_lazy, reverse
from arcana_app.forms import AddTruckForm, AddDriverForm
from arcana_app.models import Driver, Truck, Trailer, Freight, Insurance, Service
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


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


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddDriverForm
    model = Driver
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('driver_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Edit driver')

    # def get_success_url(self):
    #     super().get_success_url()
    #     return reverse('update_driver', args=(self.object.id,))


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    template_name = 'arcana_app/driver_detail.html'


class AddTruckView(LoginRequiredMixin, CreateView):
    form_class = AddTruckForm
    model = Truck
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_truck')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add truck')


class TruckListView(LoginRequiredMixin, ListView):
    model = Truck
    template_name = 'arcana_app/truck_list.html'


class TruckUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddTruckForm
    model = Truck
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('truck_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Edit truck')

    # def get_success_url(self):
    #     super().get_success_url()
    #     return reverse('update_truck', args=(self.object.id,))


class TruckDetailView(LoginRequiredMixin, DetailView):
    model = Truck
    template_name = 'arcana_app/truck_detail.html'

    def get_context_data(self, **kwargs):
        is_actual_mot = self.get_object().begin_MOT <= datetime.date.today() <= self.get_object().expire_MOT
        if is_actual_mot:
            is_actual_mot = 'Yes'
        else:
            is_actual_mot = 'No'
        return super().get_context_data(is_actual_mot=is_actual_mot)


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    template_name = 'arcana_app/truck_delete.html'
    success_url = reverse_lazy('truck_list')
