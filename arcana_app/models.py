# from django.contrib.gis.db import models
from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
import datetime
import os
from twilio.rest import Client

# DOCUMENTS or class Documents

TYPES = (
    (1, 'MEGA'),
    (2, 'STANDARD')
)

AXES = (
    (2, 'TWO'),
    (3, 'THREE')
)


class Driver(models.Model):
    id_card_type = models.CharField(max_length=128)
    id_card_nr = models.CharField(max_length=30, unique=True)
    # should i make class DrivinLicense?
    driving_license = models.FileField(upload_to='media/')
    driving_license_category = models.CharField(max_length=10)
    driving_license_begin_date = models.DateField(default=None, null=True, blank=True)
    driving_license_expiration_date = models.DateField(default=None, null=True, blank=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()
    pesel = models.CharField(max_length=11, unique=True)
    photo = models.FileField(upload_to='media/')
    visa = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    visa_begin_date = models.DateField(default=None, null=True, blank=True)
    visa_expiration_date = models.DateField(default=None, null=True, blank=True)
    medical_research = models.BooleanField()  # ????????????????!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    medical_research_file = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    medical_research_begin_date = models.DateField(default=None, null=True, blank=True)
    medical_research_expiration_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Truck(models.Model):
    photos_of_the_truck = models.FileField(upload_to='media/')
    country_of_registration = CountryField()
    registration_number = models.CharField(max_length=15, unique=True)
    registration_id_scan = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model_name = models.CharField(max_length=128)  # change to model_name
    color = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)
    type = models.IntegerField(choices=TYPES)
    quantity_of_axes = models.IntegerField(choices=AXES)
    capacity = models.IntegerField()
    exhaust_emission_certificate = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    toll_collection_device = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    toll_collection_device_model = models.CharField(max_length=30)
    toll_collection_device_serial_nr = models.CharField(max_length=15)
    toll_collection_device_operator = models.CharField(max_length=15)
    toll_collection_device_countries = CountryField(multiple=True, blank=True)  # ?????????!!!!Is that all?
    equipment = models.TextField()  # Radio, refrigerator, gps, cd,dvd, printer etc.
    begin_MOT = models.DateField()
    expire_MOT = models.DateField()
    insurance = models.ForeignKey('Insurance', on_delete=models.CASCADE, default=None, null=True, blank=True)

    # geolocation = models.PointField()

    def __str__(self):
        return self.brand + ' ' + self.model_name + ' ' + self.registration_number


class Trailer(models.Model):
    photos_of_the_truck = models.FileField(upload_to='media/')
    country_of_registration = CountryField()
    registration_number = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model_name = models.CharField(max_length=128)
    type = models.IntegerField(choices=TYPES)
    kind = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)
    begin_MOT = models.DateField()
    expire_MOT = models.DateField()
    insurance = models.ForeignKey('Insurance', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.brand + ' ' + self.type + ' ' + self.registration_number


class Insurance(models.Model):
    company_name = models.CharField(max_length=255)
    nr_of_policy = models.CharField(max_length=255, blank=False)
    begin_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    insurance_value = models.FloatField()
    is_actual = models.BooleanField(default=None)  # check it!!!!!!!!!!


class Freight(models.Model):
    name = models.CharField(max_length=255)
    nr_of_freight = models.CharField(max_length=255)
    forwarding = models.ForeignKey('Forwarding', on_delete=models.CASCADE, default=None, null=True, blank=True)
    cargo = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, default=None, null=True,
                              blank=True)  # on_delete=models.SET("Truck erased.")???
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE, default=None, null=True, blank=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, default=None, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date_of_loading = models.DateField(default=None, null=True, blank=True)
    hour_of_loading = models.TimeField(default=None, null=True, blank=True)
    date_of_unloading = models.DateField(default=None, null=True, blank=True)
    hour_of_unloading = models.TimeField(default=None, null=True, blank=True)
    loading_address_company_name = models.CharField(max_length=255)
    loading_address_company_address_street = models.CharField(max_length=255)
    loading_address_company_address_local_nr = models.CharField(max_length=255)
    loading_address_company_address_postal_code = models.CharField(max_length=255)
    loading_address_company_address_city = models.CharField(max_length=255)
    loading_address_company_address_country = models.CharField(max_length=255)
    unloading_address_company_name = models.CharField(max_length=255)
    unloading_address_company_address_street = models.CharField(max_length=255)
    unloading_address_company_address_local_nr = models.CharField(max_length=255)
    unloading_address_company_address_postal_code = models.CharField(max_length=255)
    unloading_address_company_address_city = models.CharField(max_length=255)
    unloading_address_company_address_country = models.CharField(max_length=255)

    # invoice = models.FileField() add or not add?
    # notes = models.TextField()

    def __str__(self):
        return self.name + '. ' + 'Loading: ' + self.loading_address_company_name + ' ' + str(
            self.date_of_loading) + '.' + ' Unloading: ' + self.unloading_address_company_name + ' ' + str(
            self.date_of_unloading) + '.'


class ServiceVisit(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today())
    mileage = models.IntegerField()
    what_is_fixed = models.TextField()
    what_to_do = models.TextField()  # zalecenia/comments
    total_costs = models.FloatField()
    invoice = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    #####dane adresowe oddzielnie?
    service_address_company_name = models.CharField(max_length=255)
    service_address_company_address_street = models.CharField(max_length=255)
    service_address_company_address_local_nr = models.CharField(max_length=255)
    service_address_company_address_postal_code = models.CharField(max_length=255)
    service_address_company_address_city = models.CharField(max_length=255)
    service_address_company_address_country = models.CharField(max_length=255)
    nip = models.IntegerField()
    #####


class Company(models.Model):
    international_license = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    international_license_nr = models.CharField(max_length=20)
    international_license_begin_date = models.DateField()
    international_license_expire_date = models.DateField()



# spedycja ponizej
class Forwarding(models.Model):
    pass


class Contractor(models.Model):
    pass

class Ocp(models.Model):
    ocp = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    ocp_payment_confirmation = models.FileField(upload_to='media/', default=None, null=True, blank=True)
    ocp_begin_date = models.DateField()
    ocp_expire_date = models.DateField()
    cars_refers_to = models.ManyToManyField(Truck)
