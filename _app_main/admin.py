
# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Elon_Baza

@admin.register(Elon_Baza)
class ElonBazaAdmin(ImportExportModelAdmin):
    list_display = (
        'material_name', 'material_price', 'material_owner', 
        'company_name', 'material_created_date'
    )
    search_fields = ('material_name', 'company_name', 'material_owner')
