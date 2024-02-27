from django.shortcuts import render
from .models import AboutGym, Coaches

def about(request):
    return render(request, 'main/about.html')


def index(request):
    gym = AboutGym.objects.all()
    coach = Coaches.objects.all()

    data = {
        'gym': gym,
        'coach': coach
    }

    return render(request, 'main/index.html', data)
