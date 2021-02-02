from django.urls import path
from plants import views

urlpatterns = [
    path('', views.plants_list),
]