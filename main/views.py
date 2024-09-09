from django.shortcuts import render
from .models import Barang

def show_main(request):
    list_barang = Barang.objects.all()
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E',
        'list_barang' : list_barang
    }

    return render(request, "main.html", context)

# Create your views here.
