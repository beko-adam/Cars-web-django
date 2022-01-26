from os import name
from django.urls import path
from . import views


app_name = 'browsr_cars'

urlpatterns = [
    path('', views.All_car,name='all_cars'),
    path('<int:id>', views.car_detiles,name='car_detiles'),

]