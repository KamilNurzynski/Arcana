# from django.contrib.gis.db import models
from django.db import models
from accounts.models import User
from django_countries.fields import CountryField
import datetime
import os
from twilio.rest import Client


# DOCUMENTS or class Documents


class Driver(models.Model):
    id_card_type = models.CharField(max_length=128)
    id_card_nr = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Truck(models.Model):
    country_of_registration = CountryField()
    registration_number = models.CharField(max_length=15, unique=True)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)  # zmienic nazwę z model na inną
    color = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)
    # geolocation = models.PointField()
    begin_MOT = models.DateField()
    expire_MOT = models.DateField()

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + self.registration_number

    # def save(self, *args, **kwargs):
    #     # if (self.expire_MOT - datetime.date.today()) >= 20:
    #
    #         account_sid = 'AC931cc13744e2966e9fe68736eaae9741'
    #         auth_token = '0024a27e3eff3ae261ddfb221405898d'
    #         client = Client(account_sid, auth_token)
    #
    #         message = client.messages.create(
    #             body=f"{self.color} {self.brand} with reg numbers {self.registration_number} has 20 days to MOT",
    #             from_='+16198536183',
    #             to='+48732190892'
    #         )
    #         print(message.sid)
    #         return super().save(*args, **kwargs)


class Trailer(models.Model):
    country_of_registration = models.CharField(max_length=128)
    registration_number = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)

    def __str__(self):
        return self.type + ' ' + self.registration_number


class Insurance(models.Model):
    # truck = models.ManyToManyField(Truck, through='InsuranceTruck')
    company_name = models.CharField(max_length=255)
    nr_of_policy = models.CharField(max_length=255, blank=False)
    begin_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    insurance_value = models.FloatField()


class Freight(models.Model):
    name = models.CharField(max_length=255)
    nr_of_freight = models.CharField(max_length=255)
    forwarding = models.ForeignKey('Forwarding', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    price = models.FloatField()
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)  # on_delete=models.SET("Truck erased.")???
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
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
    invoice = models.FileField()
    # notes = models.TextField()


class Service(models.Model):
    name = models.CharField(max_length=255)


# spedycja ponizej
class Forwarding(models.Model):
    pass
