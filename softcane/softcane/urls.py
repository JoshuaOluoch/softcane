"""softcane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from tenant.views import (our_vehicle_type, vehicle_type_create,
                          vehicle, vehicle_create,
                          VehicleTypeUpdateView, VehicleTypeDeleteView,
                          VehicleUpdateView, VehicleDeleteView,forgotPassword,changePassword)

admin.site.site_header = "Softcane Admin"
admin.site.site_title = "Softcane Admin Portal"
admin.site.index_title = "Welcome to Softcane Transport Management Portal"
urlpatterns = [
    path('',include('dashboard.urls'), name = 'index'),
    path('location/', include('location.urls'), name = 'location'),
    path('accounting/',include('accounting.urls'),name = 'accounting'),
    path('stock/', include('stock.urls'),name = 'stock'),
    path('hr/', include('hr.urls'), name = 'hr'),
    path('users/', include('users.urls'), name = 'users'),
    path('transport/', include('transport.urls'), name = 'transport'),
    path('report/', include('report.urls'), name='report'),
    path('configuration_vehicle_type/',our_vehicle_type, name = 'vehicle-types'),
    path('vehicle_type_create/', vehicle_type_create, name = 'vehicle_type_create'),
    path('configuration_vehicle_type/<pk>/vehicle_type_update/', VehicleTypeUpdateView.as_view(), name = 'vehicle_type_edit'),
    path('configuration_vehicle_type/<pk>/vehicle_type_delete/', VehicleTypeDeleteView.as_view(), name = 'vehicle_type_delete'),
    path('vehicle/',vehicle, name = 'vehicle'),
    path('vehicle_create/', vehicle_create, name = 'vehicle_create'),
    path('vehicle/<pk>/vehicle_update/', VehicleUpdateView.as_view(), name = 'vehicle_edit'),
    path('vehicle/<pk>/vehicle_delete/', VehicleDeleteView.as_view(), name = 'vehicle_delete'),
    path('admin/', admin.site.urls),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('changePassword/', changePassword, name='change_password'),

]
