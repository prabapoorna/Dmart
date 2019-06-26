# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import  redirect  
from django.views.decorators.csrf import csrf_exempt
import json

from forms import UserForm
from models import Post
from models import Employee


@csrf_exempt
def emp(request):  
    if request.method == "POST":  
        form = UserForm(request.POST)
        data = request.POST.copy()
        print("Inside form",form)  
        if form.is_valid():  
            try:  
                print("Inside valid")
                form.save()  
            except:  
                pass  
    else:  
        form = UserForm()  
    user_data = Employee.objects.get(uid=data.get("uid"))
    user = model_to_dict(user_data)
    return HttpResponse(json.dumps(user))



  
def showAllEmployees():
    user_data = Employee.objects.all()
    user_json = serializers.serialize('json', user_data)
    return HttpResponse(user_json, content_type='application/json')

def update(request):
    
    data = request.POST.copy()
    user = Employee.objects.get(id=data.get("uid"))



def destroy(request, id):  
    Post = Post.objects.get(id=id)  
    Post.delete()  
    return redirect("/show")  