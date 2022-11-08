from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create_user/', views.RegisterView.as_view(), name='create_user'),
    path('my_account/', views.UserAccountView.as_view(), name='my_account'),
]