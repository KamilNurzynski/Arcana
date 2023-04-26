from django.urls import path
from arcana_app import views

urlpatterns = [
    path('add_driver/', views.AddDriverView.as_view(), name='add_driver'),
    path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
    path('update_driver/<int:pk>/', views.DriverUpdateView.as_view(), name='update_driver'),
    path('driver/<int:pk>/', views.DriverDetailView.as_view(), name='detail_driver'),
    path('delete_driver/<int:pk>/', views.DriverDeleteView.as_view(), name='delete_driver'),
    path('add_truck/', views.AddTruckView.as_view(), name='add_truck'),
    path('truck_list/', views.TruckListView.as_view(), name='truck_list'),
    path('update_truck/<int:pk>/', views.TruckUpdateView.as_view(), name='update_truck'),
    path('truck/<int:pk>/', views.TruckDetailView.as_view(), name='detail_truck'),
    path('delete_truck/<int:pk>/', views.TruckDeleteView.as_view(), name='delete_truck'),
    path('add_trailer/', views.AddTrailerView.as_view(), name='add_trailer'),
    path('trailer_list/', views.TrailerListView.as_view(), name='trailer_list'),
    path('update_trailer/<int:pk>/', views.TrailerUpdateView.as_view(), name='update_trailer'),
    path('trailer/<int:pk>/', views.TrailerDetailView.as_view(), name='detail_trailer'),
    path('delete_trailer/<int:pk>/', views.TrailerDeleteView.as_view(), name='delete_trailer'),
    path('add_freight/', views.AddFreightView.as_view(), name='add_freight'),
    path('freight_list/', views.FreightListView.as_view(), name='freight_list'),
    path('update_freight/<int:pk>/', views.FreightUpdateView.as_view(), name='update_freight'),
    path('freight/<int:pk>/', views.FreightDetailView.as_view(), name='detail_freight'),
    path('delete_freight/<int:pk>/', views.FreightDeleteView.as_view(), name='delete_freight'),
    path('add_insurance/', views.AddInsuranceView.as_view(), name='add_insurance'),
]
