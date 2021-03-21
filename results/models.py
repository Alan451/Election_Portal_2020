from django.db import models
from django.contrib.auth.models import User
# Create your models here.copy
import os
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete

class keys(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    public_key = models.FileField(upload_to='public_key/',blank=True)
    private_key = models.FileField(upload_to='private_key/',blank=True)
    pubkey = models.BooleanField(default=False)
    prikey = models.BooleanField(default=False)

class notaCount(models.Model):
    CATEGORY = (
        ('VP', 'Vice President'),
        ('HAB', 'General Secretary of Hostel Affairs Board'),
        ('UGS', 'Under Graduate Senator'),
        ('PGS','Post Graduate Senator'),
        ('GS','Girl Senator'),
        ('Tech','General Secretary of Technical Board'),
        ('Cult','General Secretary of Cultural Board'),
        ('Welfare','General Secretary of Students\' Welfare Board'),
        ('Sports','General Secretary of Sports Board'),
        ('SAIL','General Seceratry of SAIL'),
        ('SWC','General Seceratry of SWC'),
    )

    post = models.CharField(max_length=7, choices=CATEGORY,unique=True)
    vote_count = models.IntegerField(default=0)

class taskid(models.Model):
    task_id = models.CharField(max_length=100,unique=True)