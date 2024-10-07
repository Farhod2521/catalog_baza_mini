from django.db import models

# Create your models here.


class Elon_Baza(models.Model):
    material_name =  models.CharField(max_length=500, blank=True, null=True)
    material_description =  models.CharField(max_length=500, blank=True, null=True)
    material_price =  models.CharField(max_length=500, blank=True, null=True)
    material_price_currency =  models.CharField(max_length=500, blank=True, null=True, default="UZS")
    material_measure =  models.CharField(max_length=500, blank=True, null=True)
    material_image =  models.CharField(max_length=500, blank=True, null=True)
    material_amount =  models.CharField(max_length=500, blank=True, null=True)
    material_amount_measure =  models.CharField(max_length=500, blank=True, null=True)
    material_status =  models.CharField(max_length=500, blank=True, null=True)
    material_created_date =  models.CharField(max_length=500, blank=True, null=True)
    material_updated_date =  models.CharField(max_length=500, blank=True, null=True)
    material_deactivated_date =  models.CharField(max_length=500, blank=True, null=True)
    sertificate_blank_num =  models.CharField(max_length=500, blank=True, null=True, default="asd123")
    sertificate_reestr_num =  models.CharField(max_length=500, blank=True, null=True, default="abs123")
    material_owner =  models.CharField(max_length=500, blank=True, null=True, default="1")
    company_name =  models.CharField(max_length=500, blank=True, null=True)
    company_stir =  models.CharField(max_length=500, blank=True, null=True)
    material_region =  models.CharField(max_length=500, blank=True, null=True)
    material_district =  models.CharField(max_length=500, blank=True, null=True)