from django.contrib import admin
from arcana_app.models import Driver, Truck, Trailer, Freight, Insurance

# Register your models here.
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Freight)
admin.site.register(Insurance)
