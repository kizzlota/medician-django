from __future__ import unicode_literals
from django.db import models
from profiles.models import DocCategories
import os
import uuid


# Create your models here.

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('user_file', filename)


class QuickRequest(models.Model):
	name = models.CharField(max_length=250, blank=True, null=True, verbose_name='name of request')
	my_own_price = models.CharField(max_length=50, blank=True, null=True, verbose_name='set own price')
	no_price = models.NullBooleanField(blank=True, null=True, verbose_name='set no price')
	symptoms = models.TextField(max_length=500, blank=True, null=True, verbose_name='short description')
	file_qr = models.FileField(blank=True, null=True, upload_to=get_file_path)
	doc_relation = models.ManyToManyField(DocCategories, blank=True, null=True, verbose_name='relation filed to Doc categories')