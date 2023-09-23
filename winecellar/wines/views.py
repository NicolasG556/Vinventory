from django.shortcuts import render, redirect

from wines.models import Vin, RegionViticole, CaveVirtuelle

from wines.forms import VinForm, RegionForm, CaveForm


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


def region_list(request):
    regions = RegionViticole.objects.all()
    return render(request,
                  'wines/region_list.html',
                  {'regions': regions})


def region_details(request, id):
    region = RegionViticole.objects.get(id=id)
    return render(request,
                  'wines/region_details.html',
                  {'region': region})


def region_create(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            # créer la region dans la base de données
            region = form.save()
            # rediriger vers la page détaillée de la région que nous venons de créer
            return redirect('region-details', region.id)

    else:
        form = RegionForm()

    return render(request,
                  'wines/region_create.html',
                  {'form': form})


def region_update(request, id):
    region = RegionViticole.objects.get(id=id)

    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            # mettre à jour la region dans la base de données
            region = form.save()
            # rediriger vers la page détaillée de la region que nous venons de mettre à jour
            return redirect('region-details', region.id)

    form = RegionForm(instance=region)  # on pré-rempli le formulaire avec une region existante
    return render(request,
                  'wines/region_update.html',
                  {'form': form})


def region_delete(request, id):
    region = RegionViticole.objects.get(id=id)

    if request.method == 'POST':
        # supprimer la region de la base de données
        region.delete()
        # rediriger vers la liste des regions
        return redirect('region-list')

        # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                  'wines/region_delete.html',
                  {'region': region})


def cave_list(request):
    caves = CaveVirtuelle.objects.all()
    return render(request,
                  'wines/cave_list.html',
                  {'caves': caves})


def cave_details(request, id):
    cave = CaveVirtuelle.objects.get(id=id)
    vins = Vin.objects.filter(id_cave=id)
    return render(request,
                  'wines/cave_details.html',
                  {'cave': cave, 'vins': vins})


def cave_create(request):
    if request.method == 'POST':
        form = CaveForm(request.POST)
        if form.is_valid():
            # créer la cave virtuelle dans la base de données
            cave = form.save()
            # rediriger vers la page détaillée de la cave virtuelle que nous venons de créer
            return redirect('cave-details', cave.id)

    else:
        form = CaveForm()

    return render(request,
                  'wines/cave_create.html',
                  {'form': form})


def cave_update(request, id):
    cave = CaveVirtuelle.objects.get(id=id)

    if request.method == 'POST':
        form = CaveForm(request.POST, instance=cave)
        if form.is_valid():
            # mettre à jour la cave virtuelle dans la base de données
            cave = form.save()
            # rediriger vers la page détaillée de la cave virtuelle que nous venons de mettre à jour
            return redirect('cave-details', cave.id)

    form = CaveForm(instance=cave)  # on pré-rempli le formulaire avec une region existante
    return render(request,
                  'wines/cave_update.html',
                  {'form': form})


def cave_delete(request, id):
    cave = CaveVirtuelle.objects.get(id=id)

    if request.method == 'POST':
        # supprimer la cave virtuelle de la base de données
        cave.delete()
        # rediriger vers la liste des caves virtuelles
        return redirect('cave-list')

        # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                  'wines/cave_delete.html',
                  {'cave': cave})
