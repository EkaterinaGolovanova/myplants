from django.urls import path
from plants import views

urlpatterns = [
    path('', views.all_plants),
]