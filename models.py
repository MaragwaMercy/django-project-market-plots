# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AdministrationPlanning(models.Model):
    adminplanid = models.AutoField(primary_key=True)
    plot_number = models.ForeignKey('Plots', models.DO_NOTHING, db_column='plot_number', blank=True, null=True)
    is_land_surveyed = models.BooleanField(blank=True, null=True)
    parcel_under_use = models.BooleanField(blank=True, null=True)
    type_of_use = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'administration_planning'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Infrastructure(models.Model):
    infraid = models.AutoField(primary_key=True)
    plot_number = models.ForeignKey('Plots', models.DO_NOTHING, db_column='plot_number', blank=True, null=True)
    water_supply = models.TextField(blank=True, null=True)  # This field type is a guess.
    electricalpower = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'infrastructure'


class Owner(models.Model):
    ownerid = models.AutoField(primary_key=True)
    plot_number = models.ForeignKey('Plots', models.DO_NOTHING, db_column='plot_number', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    no_of_children = models.IntegerField(blank=True, null=True)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    postal_address = models.CharField(max_length=100, blank=True, null=True)
    kra_pin = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Ownership(models.Model):
    ownershipid = models.AutoField(primary_key=True)
    plot_number = models.ForeignKey('Plots', models.DO_NOTHING, db_column='plot_number', blank=True, null=True)
    mode_of_acquisition = models.TextField(blank=True, null=True)  # This field type is a guess.
    ownership_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    lease_duration_from = models.DateField(blank=True, null=True)
    lease_duration_to = models.DateField(blank=True, null=True)
    pay_landrates = models.BooleanField(blank=True, null=True)
    proof_of_ownership = models.BooleanField(blank=True, null=True)
    type_of_document = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ownership'


class Plots(models.Model):
    plot_number = models.IntegerField(primary_key=True)
    parcel_area = models.FloatField(blank=True, null=True)
    allocation_number = models.CharField(db_column='Allocation_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plots'
