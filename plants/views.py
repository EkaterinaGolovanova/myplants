from django.shortcuts import render


# Create your views here.
def plants_list(request):
    return render(request, 'plants/index.html')
