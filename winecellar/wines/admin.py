from django.contrib import admin

from wines.models import CaveVirtuelle
from wines.models import RegionViticole
from wines.models import Vin
from wines.models import Cepage
from wines.models import Met


class VinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'millesime', 'id_region', 'id_cave')


admin.site.register(CaveVirtuelle)
admin.site.register(RegionViticole)
admin.site.register(Vin, VinAdmin)
admin.site.register(Cepage)
admin.site.register(Met)
