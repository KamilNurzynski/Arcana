from django.shortcuts import render, redirect
from django import forms
import datetime
from django.urls import reverse_lazy, reverse
from arcana_app.forms import AddDriverForm, AddTrailerForm, AddTruckForm, AddInsuranceForm, AddFreightForm
from arcana_app.models import Driver, Truck, Trailer, Freight, Insurance, ServiceVisit
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http.response import FileResponse
import boto3
from decouple import config
from Arcana import settings

# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


class AddDriverView(LoginRequiredMixin, CreateView):
    form_class = AddDriverForm
    model = Driver
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_driver')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add driver')


class DriverListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Driver
    template_name = 'arcana_app/driver_list.html'
    ordering = ['last_name']


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

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #     photo = self.object
    #     return FileResponse(open(song, 'rb'),
    #                         as_attachment=True,
    #                         filename=f'{song.artist} - {song.title}.mp3')

    def get_context_data(self, **kwargs):
        client = boto3.client('s3', aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY'))
        bucket_name = config('AWS_STORAGE_BUCKET_NAME')
        file_name = self.object.photo.url

        url = client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': file_name.name, },
            ExpiresIn=600, )
        return super().get_context_data(download_url= url)


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
    ordering = ['registration_number']


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


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'arcana_app/driver_delete.html'
    success_url = reverse_lazy('driver_list')


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    template_name = 'arcana_app/truck_delete.html'
    success_url = reverse_lazy('truck_list')


class AddTrailerView(LoginRequiredMixin, CreateView):
    form_class = AddTrailerForm
    model = Truck
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_trailer')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add trailer')


class TrailerListView(LoginRequiredMixin, ListView):
    model = Trailer
    template_name = 'arcana_app/trailer_list.html'
    ordering = ['registration_number']


class TrailerUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddTrailerForm
    model = Trailer
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('trailer_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Edit trailer')

    # def get_success_url(self):
    #     super().get_success_url()
    #     return reverse('update_truck', args=(self.object.id,))


class TrailerDetailView(LoginRequiredMixin, DetailView):
    model = Trailer
    template_name = 'arcana_app/trailer_detail.html'

    def get_context_data(self, **kwargs):
        is_actual_mot = self.get_object().begin_MOT <= datetime.date.today() <= self.get_object().expire_MOT
        if is_actual_mot:
            is_actual_mot = 'Yes'
        else:
            is_actual_mot = 'No'
        return super().get_context_data(is_actual_mot=is_actual_mot)


class TrailerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trailer
    template_name = 'arcana_app/trailer_delete.html'
    success_url = reverse_lazy('trailer_list')


class AddInsuranceView(LoginRequiredMixin, CreateView):
    form_class = AddInsuranceForm
    model = Insurance
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_insurance')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add insurance')


class AddFreightView(LoginRequiredMixin, CreateView):
    form_class = AddFreightForm
    model = Freight
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('add_freight')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Add freight')


class FreightListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Freight
    template_name = 'arcana_app/freight_list.html'
    # ordering = ['']


class FreightUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddFreightForm
    model = Freight
    template_name = 'arcana_app/add_objects.html'
    success_url = reverse_lazy('freight_list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(submit_value_text='Edit freight')


############################################################
class FreightDetailView(LoginRequiredMixin, DetailView):
    model = Freight
    template_name = 'arcana_app/freight_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(attrs=[key for key in Freight.__dict__.keys() if not key.startswith('_')])


############################################################
class FreightDeleteView(LoginRequiredMixin, DeleteView):
    model = Freight
    template_name = 'arcana_app/freight_delete.html'
    success_url = reverse_lazy('freight_list')
