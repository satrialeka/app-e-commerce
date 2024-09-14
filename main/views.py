from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import SneakersForm
from main.models import Sneakers

def show_main(request):
    sneakers = Sneakers.objects.all()
    return render(request, "main.html", {"sneakers": sneakers,})

def create_sneakers(request):
    form = SneakersForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_sneakers.html", context)

def show_xml(request):
    data = Sneakers.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Sneakers.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Sneakers.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Sneakers.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")