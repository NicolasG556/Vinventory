from django.shortcuts import render, redirect

from wines.models import Vin

from wines.forms import VinForm


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


def vin_create(request):
    if request.method == 'POST':
        form = VinForm(request.POST)
        if form.is_valid():
            # créer le vin dans la base de données
            vin = form.save()
            # rediriger vers la page détaillée du vin que nous venons de créer
            return redirect('vin-details', vin.id)

    else:
        form = VinForm()

    return render(request,
                  'wines/vin_create.html',
                  {'form': form})


def vin_update(request, id):
    vin = Vin.objects.get(id=id)

    if request.method == 'POST':
        form = VinForm(request.POST, instance=vin)
        if form.is_valid():
            # mettre à jour le vin dans la base de données
            vin = form.save()
            # rediriger vers la page détaillée du vin que nous venons de mettre à jour
            return redirect('vin-details', vin.id)

    form = VinForm(instance=vin)  # on pré-rempli le formulaire avec un vin existant
    return render(request,
                  'wines/vin_update.html',
                  {'form': form})


def vin_delete(request, id):
    vin = Vin.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le vin de la base de données
        vin.delete()
        # rediriger vers la liste des vins
        return redirect('vin-list')

        # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                  'wines/vin_delete.html',
                  {'vin': vin})
