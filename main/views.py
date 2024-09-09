from django.shortcuts import render
from .models import Barang

def show_main(request):
    list_barang = Barang.objects.all()
    context = {
        'npm' : '2306245094',
        'name': 'M. Satria Aleka Ramadhan',
        'class': 'PBP C',
        'list_barang' : list_barang
    }

    return render(request, "main.html", context)

# Create your views here.
