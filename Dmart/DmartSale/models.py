# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):  
    uid = models.CharField(max_length=20)  
    uname = models.CharField(max_length=100)  
    uemail = models.EmailField()  
    ucontact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "dmart_user"  
        
        
class Post(models.Model):
    pid = models.CharField(max_length=20)
    post_author = models.CharField(max_length=100)
    post_date  = models.DateField()
    post_content = models.TextField
    class Meta:
        db_table = "dmart_post"
    
    