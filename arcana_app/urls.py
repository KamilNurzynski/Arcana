from django.urls import path
from arcana_app import views

urlpatterns = [
    path('add_driver/', views.AddDriverView.as_view(), name='add_driver'),
    path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
    path('add_truck/', views.AddTruckView.as_view(), name='add_truck'),
    path('truck_list/', views.TruckListView.as_view(), name='truck_list'),
    path('update_driver/<int:pk>/', views.DriverUpdateView.as_view(), name='update_driver'),
    path('update_truck/<int:pk>/', views.TruckUpdateView.as_view(), name='update_truck'),
    path('driver/<int:pk>/', views.DriverDetailView.as_view(), name='detail_driver'),
    path('truck/<int:pk>/', views.TruckDetailView.as_view(), name='detail_truck'),
    path('delete_truck/<int:pk>/', views.TruckDeleteView.as_view(), name='delete_truck'),
    path('add_insurance/', views.AddInsuranceView.as_view(), name='add_insurance'),
]
