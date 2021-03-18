from django.urls import path
from plants import views

app_name = 'plants'

urlpatterns = [
    path('', views.all_plants, name='all_plants'),
    path('<int:pk>', views.plant_detail, name='plant_detail'),
]