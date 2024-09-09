from django.shortcuts import render
from django.http import HttpResponse
from .models import Sneakers

def show_main(request):
    sneakers = Sneakers.objects.all()

    return render(request, "main.html", {"sneakers": sneakers,})
