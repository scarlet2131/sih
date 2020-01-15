# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class login(models.Model):
	username =models.CharField(max_length=150)
	password = models.CharField(max_length=150)

class user_info(models.Model):
	name = models.CharField(max_length=150)
	username = models.CharField(max_length=150)
	password = models.CharField(max_length=150)
	phone_no = models.CharField(max_length=150)
	address = models.CharField(max_length=150)
	user_type = models.CharField(max_length=150)

class farm_details(models.Model):
	username = models.CharField(max_length=150)
	crop = models.CharField(max_length=150)
	quantity = models.CharField(max_length=150)
	status = models.CharField(max_length=150)
	date_of_entry =  models.CharField(max_length=150)
	img_crop = models.CharField(max_length=150)


