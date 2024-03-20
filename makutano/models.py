from django.db import models
from django.contrib.gis.db import models

class Plots(models.Model):
    gid = models.IntegerField(primary_key=True)
    plot_number = models.IntegerField(blank=True, null=True)
    parcel_area = models.FloatField(blank=True, null=True)
    allocation_number = models.CharField(db_column='allocation_number', max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32737, blank=True, null=True)

    def __str__(self):
        return str(self.plot_number)
    class Meta:
        managed = True
        db_table = 'plots'
        verbose_name_plural = 'plots'

class Owner(models.Model):
    ownerid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Plots, models.DO_NOTHING, db_column='gid', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    no_of_children = models.IntegerField(blank=True, null=True)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    postal_address = models.CharField(max_length=100, blank=True, null=True)
    kra_pin = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = True
        db_table = 'owner'

class Ownership(models.Model):
    ownershipid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Plots, models.DO_NOTHING, db_column='gid', blank=True, null=True)
    
    MODE_OF_ACQUISITION_CHOICES = [
        ('1', 'Inheritance'),
        ('2', 'Government allocation'),
        ('3', 'County council allocation'),
        ('4', 'First acquisition'),
        ('5', 'No idea how the land was acquired'),
        ('6', 'Others'),
    ]

    OWNERSHIP_TYPE_CHOICES = [
        ('1', 'Leasehold'),
        ('2', 'Freehold'),
        ('3', 'Allotment'),
        ('4', 'Community land'),
        ('5', 'Others'),
    ]

    mode_of_acquisition = models.CharField(max_length=100, choices=MODE_OF_ACQUISITION_CHOICES, blank=True, null=True)
    ownership_type = models.CharField(max_length=100, choices=OWNERSHIP_TYPE_CHOICES, blank=True, null=True)
    lease_duration_from = models.DateField(blank=True, null=True)
    lease_duration_to = models.DateField(blank=True, null=True)
    pay_landrates = models.BooleanField(blank=True, null=True)
    proof_of_ownership = models.BooleanField(blank=True, null=True)
    type_of_document = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.ownership_type)
    class Meta:
        managed = True
        db_table = 'ownership'

class AdministrationPlanning(models.Model):
    adminplanid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Plots, models.DO_NOTHING, db_column='gid', blank=True, null=True)
    is_land_surveyed = models.BooleanField(blank=True, null=True)
    parcel_under_use = models.BooleanField(blank=True, null=True)
    
    TYPE_OF_USE_CHOICES = [
        ('Commercial Residential', 'Commercial Residential'),
        ('Personal residential', 'Personal residential'),
        ('Commercial', 'Commercial'),
        ('Offices', 'Offices'),
        ('Institutional', 'Institutional'),
        ('Industrial', 'Industrial'),
        ('Agricultural', 'Agricultural'),
        ('Recreational', 'Recreational'),
        ('Other', 'Other'),
    ]

    type_of_use = models.CharField(max_length=100, choices=TYPE_OF_USE_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.type_of_use)
    class Meta:
        managed = True
        db_table = 'administration_planning'

class Infrastructure(models.Model):
    infraid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Plots, models.DO_NOTHING, db_column='gid', blank=True, null=True)
    
    WATER_SUPPLY_CHOICES = [
        ('1', 'Personal Piped supply'),
        ('2', 'Local government piped supply'),
        ('3', 'Community piped supply'),
        ('4', 'Water tanks'),
        ('5', 'Borehole'),
        ('6', 'Well'),
        ('7', 'River/spring'),
        ('8', 'Others'),
    ]

    ELECTRICAL_POWER_CHOICES = [
        ('1', 'National grid'),
        ('2', 'Solar energy'),
        ('3', 'Others'),
    ]

    water_supply = models.CharField(max_length=100, choices=WATER_SUPPLY_CHOICES, blank=True, null=True)
    electricalpower = models.CharField(max_length=100, choices=ELECTRICAL_POWER_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.water_supply)
    class Meta:
        managed = True
        db_table = 'infrastructure'



