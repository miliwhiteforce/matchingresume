# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidates(models.Model):
    register_from = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    current_title = models.CharField(max_length=255, blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    canddiate_state = models.CharField(max_length=255, blank=True, null=True)
    candidate_country = models.CharField(max_length=255, blank=True, null=True)
    pref_location = models.CharField(max_length=255, blank=True, null=True)
    current_ctc = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    total_exp = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    highestqualification = models.CharField(db_column='highestQualification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    database_id = models.IntegerField(blank=True, null=True)
    last_updated = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidates'


class Degrees(models.Model):
    degree_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'degrees'


class IndustryType(models.Model):
    industry_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industry_type'
