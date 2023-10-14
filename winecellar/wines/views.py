from django.db.models import Q
from django.shortcuts import render, redirect
from authentication.models import User
from wines.models import Vin, RegionViticole, CaveVirtuelle, Cepage
from wines.forms import VinForm, RegionForm, CaveForm, CepageForm, VinSearchForm
from django.contrib.auth.decorators import login_required


@login_required
def hello(request):
    return render(request,
                  'wines/hello.html')


@login_required
def vin_list(request):
    vins = Vin.objects.all()
    return render(request,
                  'wines/vin_list.html',
                  {'vins': vins})


@login_required
def vin_details(request, id):
    vin = Vin.objects.get(id=id)
    return render(request,
                  'wines/vin_details.html',
                  {'vin': vin})


@login_required
def vin_create(request, id_cave):
    cave = CaveVirtuelle.objects.get(id=id_cave)
    if request.method == 'POST':
        form = VinForm(request.POST)
        if form.is_valid():
            # créer le vin dans la base de données
            vin = form.save(commit=False)

            vin.id_cave = cave

            vin = form.save()
            # rediriger vers la page détaillée du vin que nous venons de créer
            return redirect('vin-details', vin.id)

    else:
        form = VinForm()

    return render(request,
                  'wines/vin_create.html',
                  {'form': form,
                   'cave': cave})


@login_required
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


@login_required
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


@login_required
def region_list(request):
    regions = RegionViticole.objects.all()
    return render(request,
                  'wines/region_list.html',
                  {'regions': regions})


@login_required
def region_details(request, id):
    region = RegionViticole.objects.get(id=id)
    return render(request,
                  'wines/region_details.html',
                  {'region': region})


@login_required
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


@login_required
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


@login_required
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


@login_required
def cave_list(request):
    caves = CaveVirtuelle.objects.all()
    return render(request,
                  'wines/cave_list.html',
                  {'caves': caves})


@login_required
def cave_details(request, id):
    cave = CaveVirtuelle.objects.get(id=id)
    vins = Vin.objects.filter(id_cave=id)

    # On recupere les critères de recherche depuis le formulaire
    form = VinSearchForm(request.GET)

    if form.is_valid():
        nom = form.cleaned_data.get('nom')
        millesime = form.cleaned_data.get('millesime')
        couleur = form.cleaned_data.get('couleur')

        # Construisez un objet Q pour filtrer les vins en fonction des critères
        filters = Q()

        if nom:
            filters &= Q(nom__icontains=nom)

        if millesime:
            filters &= Q(millesime=millesime)

        if couleur:
            filters &= Q(couleur=couleur)

        vins = vins.filter(filters)

    return render(request,
                  'wines/cave_details.html',
                  {'cave': cave,
                   'vins': vins,
                   'form': form})


@login_required
def cave_create(request):
    if request.method == 'POST':
        form = CaveForm(request.POST)
        if form.is_valid():
            # Create a CaveVirtuelle object but do not save it yet
            cave = form.save(commit=False)

            # Set the id_user field to the currently logged-in user
            cave.id_user = request.user

            # créer la cave virtuelle dans la base de données
            cave = form.save()

            # rediriger vers la page détaillée de la cave virtuelle que nous venons de créer
            return redirect('cave-details', cave.id)

    else:
        form = CaveForm()

    return render(request,
                  'wines/cave_create.html',
                  {'form': form})


@login_required
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


@login_required
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


@login_required
def cepage_list(request):
    cepages = Cepage.objects.all()
    return render(request,
                  'wines/cepage_list.html',
                  {'cepages': cepages})


@login_required
def cepage_details(request, id):
    cepage = Cepage.objects.get(id=id)
    return render(request,
                  'wines/cepage_details.html',
                  {'cepage': cepage})


@login_required
def cepage_create(request):
    if request.method == 'POST':
        form = CepageForm(request.POST)
        if form.is_valid():
            # créer le cepage dans la base de données
            cepage = form.save()
            # rediriger vers la page détaillée du cepage que nous venons de créer
            return redirect('cepage-details', cepage.id)

    else:
        form = CepageForm()

    return render(request,
                  'wines/cepage_create.html',
                  {'form': form})


@login_required
def cepage_update(request, id):
    cepage = Cepage.objects.get(id=id)

    if request.method == 'POST':
        form = CepageForm(request.POST, instance=cepage)
        if form.is_valid():
            # mettre à jour le cepage dans la base de données
            cepage = form.save()
            # rediriger vers la page détaillée du cepage que nous venons de mettre à jour
            return redirect('cepage-details', cepage.id)

    form = CepageForm(instance=cepage)  # on pré-rempli le formulaire avec un cepage existant
    return render(request,
                  'wines/cepage_update.html',
                  {'form': form})


@login_required
def cepage_delete(request, id):
    cepage = Cepage.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le cepage de la base de données
        cepage.delete()
        # rediriger vers la liste des cepages
        return redirect('cepage-list')

        # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                  'wines/cepage_delete.html',
                  {'cepage': cepage})


# Cartographie France

@login_required
def carte_france(request, id_cave):
    cave = CaveVirtuelle.objects.get(id=id_cave)
    regions = RegionViticole.objects.all()
    data = {}  # Créez un dictionnaire pour stocker les données que vous souhaitez passer au modèle HTML

    for region in regions:
        nb_vins_region = Vin.objects.filter(id_cave=cave, id_region=region.id).count()
        data[region] = nb_vins_region  # Associez le nombre de vins à chaque région

    return render(request,
                  'wines/carte_france.html',
                  {'regions': regions,
                   'data': data,
                   'cave': cave})
