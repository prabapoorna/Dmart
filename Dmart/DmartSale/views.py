# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect  
from django.views.decorators.csrf import csrf_exempt

from forms import PostForm
from forms import UserForm
from models import Post
from models import User


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
        form = PostForm()  
    user_data = User.objects.all()
    user_json = serializers.serialize('json', user_data)
    return HttpResponse(user_json, content_type='application/json')  
def showAllEmployees():
    post_data = User.objects.all()
    post_json = serializers.serialize('json', post_data)
    return HttpResponse(post_json, content_type='application/json')


def destroy(request, id):  
    Post = Post.objects.get(id=id)  
    Post.delete()  
    return redirect("/show")  