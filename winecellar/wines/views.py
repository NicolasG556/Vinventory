from django.shortcuts import render

from wines.models import Vin


def hello(request):
    return render(request,
                  'wines/hello.html')


def vin_list(request):
    vins = Vin.objects.all()
    return render(request,
                  'wines/vin_list.html',
                  {'vins': vins})


def vin_details(request, id):
    vin = Vin.objects.get(id=id)
    return render(request,
                  'wines/vin_details.html',
                  {'vin': vin})
