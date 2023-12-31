"""
URL configuration for winecellar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import wines.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout', LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    path('signup/', authentication.views.signup_page, name='signup'),
    path('update_user/<int:user_id>/', authentication.views.update_user, name='update-user'),
    path('user_list/', authentication.views.user_list, name='user-list'),

    path('hello/', wines.views.hello, name='hello'),
    path('vins/', wines.views.vin_list, name='vin-list'),
    path('vins/<int:id>/', wines.views.vin_details, name='vin-details'),
    path('cave/<int:id_cave>/vins/add/', wines.views.vin_create, name='vin-create'),
    path('vins/<int:id>/update', wines.views.vin_update, name='vin-update'),
    path('vins/<int:id>/delete', wines.views.vin_delete, name='vin-delete'),

    path('regions/', wines.views.region_list, name='region-list'),
    path('regions/<int:id>/', wines.views.region_details, name='region-details'),
    path('regions/add/', wines.views.region_create, name='region-create'),
    path('regions/<int:id>/update', wines.views.region_update, name='region-update'),
    path('regions/<int:id>/delete', wines.views.region_delete, name='region-delete'),

    path('caves/', wines.views.cave_list, name='cave-list'),
    path('caves/<int:id>/', wines.views.cave_details, name='cave-details'),
    path('caves/add/', wines.views.cave_create, name='cave-create'),
    path('caves/<int:id>/update', wines.views.cave_update, name='cave-update'),
    path('caves/<int:id>/delete', wines.views.cave_delete, name='cave-delete'),

    path('cepages/', wines.views.cepage_list, name='cepage-list'),
    path('cepages/<int:id>/', wines.views.cepage_details, name='cepage-details'),
    path('cepages/add/', wines.views.cepage_create, name='cepage-create'),
    path('cepages/<int:id>/update', wines.views.cepage_update, name='cepage-update'),
    path('cepages/<int:id>/delete', wines.views.cepage_delete, name='cepage-delete'),

    path('evenements/', wines.views.evenement_list, name='evenement-list'),
    path('evenements/<int:id>/', wines.views.evenement_details, name='evenement-details'),
    path('evenements/add/', wines.views.evenement_create, name='evenement-create'),
    path('evenements/<int:id>/update', wines.views.evenement_update, name='evenement-update'),
    path('evenements/<int:id>/delete', wines.views.evenement_delete, name='evenement-delete'),

    path('admin_page/', wines.views.admin_page, name='admin-page'),

    path('photo/upload/', wines.views.photo_upload, name='photo_upload'),

    path('cave/<int:id_cave>/carte/', wines.views.carte_france, name='carte-france'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
