"""
URL configuration for petfect_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views as auth_views
from clientsApp import views as clients_views
from employeesApp import views as employees_views
from servicesApp import views as services_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/roles/<int:pk>/', auth_views.RoleDetailView.as_view()),
    path('api/v1/roles/', auth_views.RoleCreateView.as_view()),
    path('api/v1/users/', auth_views.UserCreateView.as_view()),
    path('api/v1/users/<str:email>/', auth_views.UserChangeRoleView.as_view()),
    path('api/v1/users/<str:email>/activate/', auth_views.UserUpdateStateView.as_view()),
    path('api/v1/auth/login/', auth_views.LoginView.as_view()),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view()),
    path('api/v1/clients/', clients_views.ClientCreateView.as_view()),
    path('api/v1/clients/<str:pk>/', clients_views.ClientDetailView.as_view()),
    path('api/v1/clients_pets/', clients_views.PetDetailView.as_view()),
    path('api/v1/clients_pets/<str:pk>/', clients_views.PetDetailView.as_view()),
    path('api/v1/clients_pets/detail/<str:pk>/', clients_views.PetView.as_view()),
    path('api/v1/employees/speciality/', employees_views.SpecialityView.as_view()),
    path('api/v1/employees/speciality/<int:pk>/', employees_views.SpecialityDetailView.as_view()),
    path('api/v1/employees/', employees_views.EmployeeView.as_view()),
    path('api/v1/employees/<str:pk>/', employees_views.EmployeeDetailView.as_view()),
    path('api/v1/employees_speciality/<str:pk>/', employees_views.EmployeeSpecialityView.as_view()),
    path('api/v1/services/', services_views.ServiceView.as_view()),
    path('api/v1/services/<str:pk>/', services_views.ServiceDetailView.as_view()),
    path('api/v1/combos/', services_views.ComboView.as_view()),
    path('api/v1/combos/<str:pk>/', services_views.ComboDetailView.as_view()),
]
