from django.shortcuts import render
from plants.models import Plant


# Create your views here.
def all_plants(request):
    # query the db to return all plant objects
    plants = Plant.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})

def plant_detail(request, pk):
    plant = Plant.objects.get(pk=pk)
    return render(request, 'plants/detail.html', {'plant': plant})


