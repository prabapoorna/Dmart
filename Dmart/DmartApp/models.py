# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(unique=True,max_length=254)  
    eemail = models.EmailField(unique=True)  
    emobile = models.CharField(unique=True,max_length=20)
    esalary =   models.CharField(max_length=20)
    erole = models.CharField(max_length=150)
    etype = models.CharField(max_length=150)
    ebranch = models.CharField(max_length=150)
    
    
    
    def __str__(self):
        return "EID : "+self.eid +" eNAME"+self.ename+" eCONTACT"+self.econtact+"eEMAIL"+self.eemail
    
    class Meta:  
        db_table = "dmart_employee"  
        


class Product(models.Model):

    def __str__(self):
        return models.Model.__str__(self)

    pid = models.AutoField(primary_key=True)
    pname = models.CharField(unique=True,max_length=254) 
    pcompany = models.CharField(max_length=15)        
    pbuyprice = models.FloatField()
    psellprice = models.FloatField()
    pdiscount = models.FloatField()
    pexpirydate = models.CharField(max_length=25)
    pquantity = models.FloatField()
    puom = models.CharField(max_length=20)
    
    class Meta:  
        db_table = "dmart_product"  
        
        
class Post(models.Model):
    pid = models.CharField(max_length=20)
    post_author = models.CharField(max_length=100)
    post_date  = models.DateField()
    post_content = models.TextField
    class Meta:
        db_table = "dmart_post"
        
        
    
    