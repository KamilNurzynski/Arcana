from django.db import models
from accounts.models import User


# Create your models here.
class Driver(models.Model):
    id_card_type = models.CharField(max_length=128)
    id_card_nr = models.CharField(max_length=30)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Truck(models.Model):
    country_of_registration = models.CharField(max_length=128)
    registration_number = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)

    # MOT = zakres dat
    # geolocation

    def __str__(self):
        return self.brand + ' ' + self.registration_number


class Trailer(models.Model):
    country_of_registration = models.CharField(max_length=128)
    registration_number = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    vin_nr = models.CharField(max_length=17)
    # MOT = zakres dat

    def __str__(self):
        return self.type + ' ' + self.registration_number


class Insurance(models.Model):
    pass


class Freight(models.Model):
    name = models.CharField(max_length=255)
    nr_of_freight = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    price = models.FloatField()
    truck = models.ForeignKey(Truck)  # on_delete=models.CASCADE???
    trailer = models.ForeignKey(Trailer)
    insurance = models.ForeignKey(Insurance)
    invoice = models.FileField()
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


class Service(models.Model):
    pass


# spedycja ponizej
class Forwarding(models.Model):
    pass
