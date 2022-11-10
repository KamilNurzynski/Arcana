from django.urls import path
from arcana_app import views

urlpatterns = [
    path('add_driver/', views.AddDriverView.as_view(), name='add_driver'),
    path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
    path('add_truck/', views.AddTruckView.as_view(), name='add_truck'),
    path('truck_list/', views.TruckListView.as_view(), name='truck_list'),
]
